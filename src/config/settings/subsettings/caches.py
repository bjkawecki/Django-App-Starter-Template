from config.settings.common import DEBUG
from config.settings.utils import get_env_variable

if DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://redis:6379",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            }
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": get_env_variable("CELERY_BROKER_URL"),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            }
        }
    }
