from config.settings.common import BASE_DIR

FORMATTERS = (
    {
        "verbose": {
            "format": "{levelname} {asctime:s} {threadName} {thread:d} {module} {filename} {lineno:d} \
                {name} {funcName} {process:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime:s} {module} {filename} {lineno:d} {funcName} {message}",
            "style": "{",
        },
        "color": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s[%(levelname)s] %(asctime)s {%(filename)s:%(lineno)d} :: %(message)s",
            "log_colors": {
                "DEBUG": "red",
                "INFO": "cyan",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        },
    },
)

HANDLERS = {
    "console_handler": {
        "class": "logging.StreamHandler",
        "formatter": "color",
    },
    "handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/normal_handler.log",  # noqa : F821
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "simple",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 5,  # 5MB
    },
    "handler_detailed": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/detailed_handler.log",  # noqa : F821
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 5,  # 5MB
    },
}

LOGGERS = (
    {
        "debug": {
            "handlers": ["console_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django": {
            "handlers": ["console_handler", "handler_detailed"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["handler", "console_handler"],
            "level": "WARNING",
            "propagate": False,
        },
    },
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS[0],
    "handlers": HANDLERS,
    "loggers": LOGGERS[0],
}
