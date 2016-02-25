# -*- coding: utf-8 -*-

import os.path
import posixpath
import sys

from django.core.urlresolvers import reverse_lazy


def env_or_default(NAME, default):
    return os.environ.get(NAME, default)

# Top level of our source / repository
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir, os.pardir))
# Symposion package
PACKAGE_ROOT = os.path.join(PROJECT_ROOT, "djangocon")

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    ('DjangoCon Web Team', 'webteam@djangocon.us'),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",  # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "djangocon2015",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
]
STATICFILES_STORAGE = 'djangocon.core.gzip_storage.GZIPPipelineStorage'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "opbeat.contrib.django.middleware.OpbeatAPMMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    'waffle.middleware.WaffleMiddleware',
    "reversion.middleware.RevisionMiddleware",
    "django.middleware.gzip.GZipMiddleware",
]

ROOT_URLCONF = "djangocon.urls"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pinax_utils.context_processors.settings",
    "pinax_theme_bootstrap.context_processors.theme",
    "account.context_processors.account",
    "symposion.reviews.context_processors.reviews",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # theme
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",
    "bootstrapform",

    # external
    "opbeat.contrib.django",
    "biblion",
    "south",
    "mailer",
    "timezones",
    "metron",
    "markitup",
    "taggit",
    "reversion",
    "easy_thumbnails",
    "sitetree",
    "account",
    "model_utils",
    "pipeline",
    "waffle",

    # symposion
    "symposion",
    "symposion.sponsorship",
    "symposion.conference",
    "symposion.cms",
    "symposion.boxes",
    "symposion.proposals",
    "symposion.speakers",
    "symposion.teams",
    "symposion.reviews",
    "symposion.schedule",

    # project
    "djangocon.core",
    "djangocon.proposals",
]

OPBEAT = {
    "ORGANIZATION_ID": os.environ.get("OPBEAT_ORG_ID"),
    "APP_ID": os.environ.get("OPBEAT_APP_ID"),
    "SECRET_TOKEN": os.environ.get("OPBEAT_SECRET_TOKEN")
}

EB_APP_KEY = os.environ.get('EB_APP_KEY')
EB_EVENT_ID = os.environ.get('EB_EVENT_ID')
EB_USER_KEY = os.environ.get('EB_USER_KEY')

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

EMAIL_BACKEND = "mailer.backend.DbBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USER_DISPLAY = lambda user: user.email

AUTHENTICATION_BACKENDS = [
    # Permissions Backends
    "symposion.teams.backends.TeamPermissionsBackend",

    # Auth backends
    "account.auth_backends.EmailAuthenticationBackend",
]

LOGIN_URL = reverse_lazy("account_login")  # NOTE: won't need reverse_lazy in Django 1.5

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

MARKITUP_SET = "markitup/sets/markdown"
MARKITUP_FILTER = ["symposion.markdown_parser.parse", {}]
MARKITUP_SKIN = "markitup/skins/simple"

CONFERENCE_ID = 1

# adjust for number of reviews currenly about 1/5 (default: 3)
SYMPOSION_VOTE_THRESHOLD = 5

SYMPOSION_PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/"

PROPOSAL_FORMS = {
    "tutorial": "djangocon.proposals.forms.TutorialProposalForm",
    "talk-25-min": "djangocon.proposals.forms.TalkProposalForm",
    "talk-45-min": "djangocon.proposals.forms.TalkProposalForm",
    "open-space": "djangocon.proposals.forms.OpenSpaceProposalForm",
}


METRON_SETTINGS = {
    "google": {
        3: os.environ.get("GA_TOKEN"),
    },
    "gauges": {
        3: os.environ.get("GAUGES_TOKEN")
    },
    "mixpanel": {
        3: os.environ.get("MIXPANEL_API_TOKEN"),
    }
}

SESSION_COOKIE_NAME = "DJANGOCON2015"

THEME_CONTACT_EMAIL = 'webteam@djangocon.us'
SERVER_EMAIL = ''

SOUTH_MIGRATION_MODULES = {
    'proposals': 'djangocon.proposals.migrations',
    'waffle': 'waffle.south_migrations',
}

COMPS_DIR = os.path.join(PACKAGE_ROOT, "templates/comps")
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
# Find virtualenv `bin` directory on Gondor
PIPELINE_CSSMIN_BINARY = os.path.join(os.path.dirname(sys.executable),
                                      'cssmin')
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.slimit.SlimItCompressor'
from .pipeline_settings import *
