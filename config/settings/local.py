from .base import *
import environ

root = environ.Path(__file__) - 3
env_file = str(root.path('.env'))
env = environ.Env()
env.read_env(env_file)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
A_TEST = env('A_TEST')
TEST = env('TEST')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
