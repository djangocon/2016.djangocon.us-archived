import base64
import io
import json
import mimetypes
import os
import uuid

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import Storage
from django.utils.functional import SimpleLazyObject

import dateutil.parser
import httplib2

from googleapiclient.discovery import build as discovery_build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from oauth2client.client import SERVICE_ACCOUNT, GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials


def _gcs_file_storage_settings():
    config = getattr(settings, "GCS_FILE_STORAGE", {})

    def default_bucket():
        try:
            return os.environ["GCS_BUCKET"]
        except KeyError:
            raise ImproperlyConfigured("Either GCS_FILE_STORAGE[bucket] or env var GCS_BUCKET need to be set.")
    config.setdefault("bucket", SimpleLazyObject(default_bucket))

    return config


class GoogleCloudStorage(Storage):
    """
    Django storage backend for Google Cloud Storage (GCS)

    This storage backend uses google-api-python-client to interact with GCS. It
    makes no assumptions about your environment and can be used anywhere.

    Current State: this class only supports uploading data to GCS (read will be
    implemented soon).

    This class is planned to be moved into its own app (or in django-storages,
    possibly). If you come across a bug with this class, contact Brian Rosner.
    """

    def __init__(self):
        self.set_client()
        self.bucket = _gcs_file_storage_settings()["bucket"]

    def set_client(self):
        credentials = self.get_oauth_credentials()
        http = credentials.authorize(httplib2.Http())
        self.client = discovery_build("storage", "v1", http=http)

    def get_oauth_credentials(self):
        return self.create_scoped(GoogleCredentials.get_application_default())

    def create_scoped(self, credentials):
        return credentials.create_scoped(["https://www.googleapis.com/auth/devstorage.read_write"])

    def execute_req(self, req):
        return req.execute()

    def get_gcs_object(self, name):
        req = self.client.objects().get(bucket=self.bucket, object=name)
        try:
            return req.execute()
        except HttpError as exc:
            if exc.resp["status"] == "404":
                return None
            raise

    # Django Storage interface

    def _open(self, name, mode):
        if mode != "rb":
            raise ValueError("rb is the only acceptable mode for this backend")
        # @@@ reading files from GCS is extremely inefficient; fix me
        # however, for small files, who cares right? ;-)
        req = self.client.objects().get_media(bucket=self.bucket, object=name)
        buf = io.BytesIO()
        media = MediaIoBaseDownload(buf, req)
        done = False
        while not done:
            done = media.next_chunk()[1]
        buf.seek(0)
        return buf

    def _save(self, name, content):
        mimetype, _ = mimetypes.guess_type(name)
        if mimetype is None:
            mimetype = "application/octet-stream"
        media = MediaIoBaseUpload(content, mimetype)
        req = self.client.objects().insert(
            bucket=self.bucket,
            name=name,
            media_body=media,
        )
        self.execute_req(req)
        return name

    def delete(self, name):
        req = self.client.objects().delete(bucket=self.bucket, object=name)
        self.execute_req(req)

    def exists(self, name):
        return self.get_gcs_object(name) is not None

    def size(self, name):
        return int(self.get_gcs_object(name)["size"])

    def url(self, name):
        url_template = _gcs_file_storage_settings().get(
            "url-template",
            "https://storage.googleapis.com/{bucket}/{name}"
        )
        return url_template.format(bucket=self.bucket, name=name)

    def accessed_time(self, name):
        return self.modified_time(name)

    def created_time(self, name):
        return dateutil.parser.parse(self.get_gcs_object(name)["timeCreated"])

    def modified_time(self, name):
        return dateutil.parser.parse(self.get_gcs_object(name)["updated"])


class ECGoogleCloudStorage(GoogleCloudStorage):
    """
    Custom subclass of GoogleCloudStorage to interact with Eldarion Cloud

    To create:

        ec instances env GCS_CREDENTIALS=$(cat key.json | base64) GCS_BUCKET=<bucket>

    """

    def get_oauth_credentials(self):
        client_credentials = json.loads(base64.b64decode(os.environ["GCS_CREDENTIALS"]))
        if client_credentials["type"] == SERVICE_ACCOUNT:
            creds = ServiceAccountCredentials.from_json_keyfile_dict(client_credentials)
        else:
            raise ImproperlyConfigured("non-service accounts are not supported")
        return self.create_scoped(creds)
