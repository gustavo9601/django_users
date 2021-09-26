from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_usuarios',
        'USER': 'django_usuarios',
        'PASSWORD': 'Pruebas1234*',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
