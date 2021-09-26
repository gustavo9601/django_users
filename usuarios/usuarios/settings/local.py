from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_settings('DEBUG')

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_settings('NAME'),
        'USER': get_settings('USER'),
        'PASSWORD': get_settings('PASSWORD'),
        'HOST': get_settings('HOST'),
        'PORT': get_settings('PORT')
    }
}
