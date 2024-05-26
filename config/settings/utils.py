import logging
import os

logger = logging.getLogger("django")


def get_env_variable(var_name, *args):
    try:
        return os.environ.get(var_name, *args)   # noqa : F821
    except KeyError as e:
        logger.error(e)
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)   # noqa : F821
