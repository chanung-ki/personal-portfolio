from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]