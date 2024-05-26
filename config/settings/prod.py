import socket

from dotenv import load_dotenv

from config.settings.subsettings.apps import APPS, DJANGO_APPS, THIRD_PARTY_APPS
from config.settings.subsettings.middleware import CUSTOM_MIDDLEWARE, MIDDLEWARE
from config.settings.utils import get_env_variable

load_dotenv()
STAGE = get_env_variable("STAGE", "False").lower() == "true"
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS

MIDDLEWARE = MIDDLEWARE + CUSTOM_MIDDLEWARE

CSRF_TRUSTED_ORIGINS = get_env_variable("CSRF_TRUSTED_ORIGINS").split(",")
CSRF_ALLOWED_ORIGINS = get_env_variable("CSRF_ALLOWED_ORIGINS").split(",")
CORS_ORIGINS_WHITELIST = get_env_variable("CORS_ORIGINS_WHITELIST").split(",")

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
