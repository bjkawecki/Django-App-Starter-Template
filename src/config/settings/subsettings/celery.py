from config.settings.common import DEBUG
from config.settings.utils import get_env_variable

if DEBUG:
    CELERY_BROKER_URL = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_ENABLE_UTC = False

else:
    CELERY_BROKER_URL = get_env_variable("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = get_env_variable("CELERY_RESULT_BACKEND")
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_ENABLE_UTC = False
