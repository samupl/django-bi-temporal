# Minimalistic django settings used to run tests
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "=" * 50

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django_bi_temporal",
    "example_app",
]

ROOT_URLCONF = __name__

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

TIME_ZONE = "UTC"
USE_I18N = False
USE_TZ = True

urlpatterns = []

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
