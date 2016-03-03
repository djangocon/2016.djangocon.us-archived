import os
import dj_database_url

from unipath import FSPath as Path


def env_or_default(NAME, default):
    return os.environ.get(NAME, default)


PROJECT_ROOT = Path(__file__).ancestor(3)
PACKAGE_ROOT = PROJECT_ROOT.child('djangocon')

BASE_DIR = PACKAGE_ROOT

DEBUG = bool(int(os.environ.get("DEBUG", "1")))

DATABASES = {
    "default": dj_database_url.config(default="postgres://localhost/djangocon2016")
}

ALLOWED_HOSTS = [
    os.environ.get("GONDOR_INSTANCE_DOMAIN"),
    "2016.djangocon.us",
    "www.djangocon.us",
    "localhost',"
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child("site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_ROOT.child("site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    PROJECT_ROOT.child("build"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
# Make this unique, and don't share it with anybody.
SECRET_KEY = "6r&z0i#!k-thu4nv^zzx!f$fbp(&#2i5mq_^%%@ihu_qxxotl_"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PACKAGE_ROOT.child("templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.core.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "symposion.reviews.context_processors.reviews",
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djangocon.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "djangocon.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # external
    "account",
    "easy_thumbnails",
    "taggit",
    "reversion",
    "metron",
    "sitetree",
    "pinax.boxes",
    "pinax.eventlog",
    "pinax.pages",
    "pinax.blog",
    "markitup",

    # symposion
    "symposion",
    "symposion.conference",
    "symposion.proposals",
    "symposion.reviews",
    "symposion.schedule",
    "symposion.speakers",
    "symposion.sponsorship",
    "symposion.teams",

    # project
    "djangocon",
    "djangocon.proposals"
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    PROJECT_ROOT.child("fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True

AUTHENTICATION_BACKENDS = [
    "symposion.teams.backends.TeamPermissionsBackend",
    "account.auth_backends.UsernameAuthenticationBackend",
]

# Symposion settings

CONFERENCE_ID = 1
PROPOSAL_FORMS = {
    "tutorial": "djangocon.proposals.forms.TutorialProposalForm",
    "talk-25-min": "djangocon.proposals.forms.TalkProposalForm",
    "talk-45-min": "djangocon.proposals.forms.TalkProposalForm",
    "open-space": "djangocon.proposals.forms.OpenSpaceProposalForm",
}
PINAX_PAGES_HOOKSET = "djangocon.hooks.PinaxPagesHookSet"
PINAX_BOXES_HOOKSET = "djangocon.hooks.PinaxBoxesHookSet"

# adjust for number of reviews currenly about 1/5 (default: 3)
SYMPOSION_VOTE_THRESHOLD = 3

MARKITUP_SET = "markitup/sets/markdown"
MARKITUP_FILTER = ["symposion.markdown_parser.parse", {}]
MARKITUP_SKIN = "markitup/skins/simple"
