"""
Contains settings for only production environment.
"""
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["junior-dev.samip.dev"]