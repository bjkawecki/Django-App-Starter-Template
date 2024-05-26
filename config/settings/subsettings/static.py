import os

from config.settings.common import BASE_DIR
from config.settings.utils import get_env_variable

COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_ENABLED = True


STATICFILES_FINDERS = (
    "compressor.finders.CompressorFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # noqa : F821
]


USE_S3 = get_env_variable("USE_S3").lower() == "true"


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # noqa : F821

if USE_S3:
    COMPRESS_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
        },
    }

    AWS_ACCESS_KEY_ID = "DO00ZRZCMZBFF8J9VTAF"
    AWS_SECRET_ACCESS_KEY = "SlQ/7Hwm2+0bfbnAwuNrYNylAQK7BCZO1dG9YdYW0Es"

    AWS_STORAGE_BUCKET_NAME = ""

    AWS_S3_CUSTOM_DOMAIN = ""

    AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    ADMIN_MEDIA_PREFIX = "/static/admin/"
    AWS_LOCATION = "static"
    AWS_QUERYSTRING_AUTH = False
    STATIC_URL = "{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }

    AWS_DEFAULT_ACL = "public-read"


else:
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    STATIC_URL = "/static/"
    STATIC_ROOT = get_env_variable("STATIC_ROOT")

    # STATIC_ROOT = "/usr/src/app/staticfiles"
