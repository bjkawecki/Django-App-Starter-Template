from config.settings.common import DEBUG
from config.settings.utils import get_env_variable

if DEBUG:
    EMAIL_HOST = "django.core.mail.backends.console.EmailBackend"
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = "testing@example.com"

else:
    EMAIL_USE_TLS = bool(get_env_variable("EMAIL_USE_TLS"))
    EMAIL_HOST = get_env_variable("EMAIL_HOST")
    EMAIL_PORT = int(get_env_variable("EMAIL_PORT"))
    EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
    EMAIL_DISPLAY_NAME = get_env_variable("EMAIL_DISPLAY_NAME")
    EMAIL_DEFAULT_FROM = get_env_variable("EMAIL_DEFAULT_FROM")
    EMAIL_SERVER_EMAIL = get_env_variable("EMAIL_SERVER_EMAIL")
    DEFAULT_FROM_EMAIL = get_env_variable("DEFAULT_FROM_EMAIL")
