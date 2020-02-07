"""
Contains settings for only development environment.
Note: DEBUG is already set to True in defaults.
"""
from .base import *

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ["127.0.0.1"]


# Debug Toolbar
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# Cors Headers
INSTALLED_APPS.append("corsheaders")
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")
CORS_ORIGIN_ALLOW_ALL = True