import os
import urlparse

from .base import *

DEBUG = False
GONDOR_INSTANCE = os.environ.get("GONDOR_INSTANCE", None)

ALLOWED_HOSTS = [
    'tl837.us2.gondor.io'
    '2016.djangocon.us',
    'djangocon.us',
    'www.djangocon.us',
]

if "GONDOR_DATABASE_URL" in os.environ:
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["GONDOR_DATABASE_URL"])
    DATABASES = {
        "default": {
            "ENGINE": {
                "postgres": "django.db.backends.postgresql_psycopg2"
            }[url.scheme],
            "NAME": url.path[1:],
            "USER": url.username,
            "PASSWORD": url.password,
            "HOST": url.hostname,
            "PORT": url.port
        }
    }

if "GONDOR_REDIS_URL" in os.environ:
    urlparse.uses_netloc.append("redis")
    url = urlparse.urlparse(os.environ["GONDOR_REDIS_URL"])
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

if GONDOR_INSTANCE == 'develop':
    CDN_URL = "http://staging.djangocon.us.global.prod.fastly.net/"
elif GONDOR_INSTANCE == 'primary':
    CDN_URL = "//djangocon-us.global.ssl.fastly.net/"
else:
    CDN_URL = "/"

STATIC_URL = CDN_URL + "site_media/static/"
MEDIA_URL = CDN_URL + "site_media/media/"

MEDIA_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "media")
STATIC_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "static")

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

FILE_UPLOAD_PERMISSIONS = 0640

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
        'opbeat': {
            'level': 'WARNING',
            'class': 'opbeat.contrib.django.handlers.OpbeatHandler',
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

DEFAULT_FROM_EMAIL = "DjangoCon 2016 <noreply@djangocon.us>"

if "GONDOR_SENDGRID_USER" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = os.environ["GONDOR_SENDGRID_USER"]
    EMAIL_HOST_PASSWORD = os.environ["GONDOR_SENDGRID_PASSWORD"]
    EMAIL_USE_TLS = True


SECRET_KEY = os.environ["SECRET_KEY"]
