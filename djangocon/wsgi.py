import os

os.environ.setdefault("DEBUG", "0")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocon.settings")

from django.core.wsgi import get_wsgi_application  # noqa

from whitenoise.django import DjangoWhiteNoise  # noqa

application = DjangoWhiteNoise(get_wsgi_application())
