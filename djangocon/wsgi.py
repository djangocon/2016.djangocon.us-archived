import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocon.settings.local")

from barrel import cooper
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

username = os.environ.get('BARREL_USER', None)
password = os.environ.get('BARREL_PASS', None)

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

if username and password:

    auth_decorator = cooper.basicauth(
        users=[(username, password), ],
        realm='Password Protected'
    )

    application = auth_decorator(application)
