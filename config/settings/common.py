from pathlib import Path

from dotenv import load_dotenv

from config.settings.utils import get_env_variable

load_dotenv()  # noqa : F821

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS").split(",")


RUN_SERVER_PORT = 8000

DEBUG = get_env_variable("DEBUG", False).lower() == "true"
VERSION = get_env_variable("VERSION")

if DEBUG:
    ADMIN_URL = "admin"
else:
    ADMIN_URL = get_env_variable("ADMIN_URL")


SITE_ID = 1

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000  # higher than the count of fields
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"
LANGUAGE_CODE = "de-de"
USE_TZ = True
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SUSPEND_SIGNALS = False
