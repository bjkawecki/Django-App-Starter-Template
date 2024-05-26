import os  # noqa : F401

import colorlog  # noqa : F401
from dotenv import load_dotenv  # noqa : F401
from split_settings.tools import include

from config.settings.common import DEBUG

if DEBUG is True:
    include(
        "common.py",
        "dev.py",
        "subsettings/auth.py",
        "subsettings/caches.py",
        "subsettings/celery.py",
        "subsettings/database.py",
        "subsettings/debug.py",
        "subsettings/email.py",
        "subsettings/log.py",
        "subsettings/messages.py",
        "subsettings/static.py",
        "subsettings/templates.py",
    )
if DEBUG is False:
    include(
        "common.py",
        "prod.py",
        "subsettings/auth.py",
        "subsettings/caches.py",
        "subsettings/celery.py",
        "subsettings/database.py",
        "subsettings/email.py",
        "subsettings/log.py",
        "subsettings/messages.py",
        "subsettings/static.py",
        "subsettings/templates.py",
    )
