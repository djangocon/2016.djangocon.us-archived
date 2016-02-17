from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*c1&^)1png^2xuta8wxm**-d*18gw$upjagp$diiz&q^5y=9gp'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'wagtail.contrib.wagtailstyleguide',
)

try:
    from .local import *
except ImportError:
    pass
