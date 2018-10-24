from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
print(os.environ.keys())
print(os.environ["DJANGO_SETTINGS_MODULE"])
DEBUG = os.environ['DEBUG']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
