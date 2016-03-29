from .gondor import *  # noqa

DEBUG = True

CDN_URL = os.environ.get("CDN_URL", "/")
STATIC_URL = CDN_URL + "site_media/static/"
MEDIA_URL = CDN_URL + "site_media/media/"

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

FILE_UPLOAD_PERMISSIONS = 0o640

DEFAULT_FILE_STORAGE = "djangocon.storage.ECGoogleCloudStorage"
