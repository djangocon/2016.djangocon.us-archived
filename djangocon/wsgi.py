import os

os.environ.setdefault("DEBUG", "0")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocon.settings")

from django.core.wsgi import get_wsgi_application  # noqa

from dj_static import Cling, MediaCling  # noqa

application = Cling(MediaCling(get_wsgi_application()))
