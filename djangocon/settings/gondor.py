import os
import urlparse

import dj_database_url

from .base import *  # noqa


DEBUG = False
GONDOR_INSTANCE = os.environ.get("GONDOR_INSTANCE", None)

ALLOWED_HOSTS = [
    '2016.djangocon.us',
    'djangocon.us',
    'www.djangocon.us',
]
if 'GONDOR_INSTANCE_DOMAIN' in os.environ:
    ALLOWED_HOSTS.append(os.environ['GONDOR_INSTANCE_DOMAIN'])

DATABASES = {
    "default": dj_database_url.config()
}

if "REDIS_URL" in os.environ:
    urlparse.uses_netloc.append("redis")
    url = urlparse.urlparse(os.environ["REDIS_URL"])
    CACHES = {
        "default": {
            "BACKEND": "redis_cache.RedisCache",
            "LOCATION": "%s:%s" % (url.hostname, url.port),
            "OPTIONS": {
                "DB": 0,
                "PASSWORD": url.password,
                "PARSER_CLASS": "redis.connection.HiredisParser"
            },
        },
    }

# Set SSL Header on environments that expect it.
if "GONDOR_HTTPS" in os.environ:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SITE_ID = int(os.environ.get("SITE_ID", "1"))

CDN_URL = os.environ.get("CDN_URL", "/")
STATIC_URL = CDN_URL + "site_media/static/"
MEDIA_URL = CDN_URL + "site_media/media/"

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

FILE_UPLOAD_PERMISSIONS = 0o640

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "propagate": True,
        },
        'opbeat.errors': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

DEFAULT_FROM_EMAIL = "DjangoCon US 2016 <noreply@djangocon.us>"

if "GONDOR_SENDGRID_USER" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 2525
    EMAIL_HOST_USER = os.environ["GONDOR_SENDGRID_USER"]
    EMAIL_HOST_PASSWORD = os.environ["GONDOR_SENDGRID_PASSWORD"]
    EMAIL_USE_TLS = True


SECRET_KEY = os.environ["SECRET_KEY"]
DEFAULT_HTTP_PROTOCOL = 'https'

DEFAULT_FILE_STORAGE = "djangocon.storage.ECGoogleCloudStorage"
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

# Fix document downloads
USE_X_ACCEL_REDIRECT = True
