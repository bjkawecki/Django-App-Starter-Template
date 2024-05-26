DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.staticfiles",
]

DEV_APPS = [
    "debug_toolbar",
]

THIRD_PARTY_APPS = [
    "django_celery_beat",
    "django_cleanup.apps.CleanupConfig",
    "django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig",
    "django_extensions",
    "django_htmx",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "compressor",
]

APPS = ["dj_app"]
