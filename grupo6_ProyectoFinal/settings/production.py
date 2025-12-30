from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['testingacc.pythonanywhere.com']
ALLOWED_HOSTS = [
    'dexter662.pythonanywhere.com',
    'www.dexter662.pythonanywhere.com',
]

#Seguridad
CSRF_TRUSTED_ORIGINS = [
    'https://dexter662.pythonanywhere.com',
    'https://www.dexter662.pythonanywhere.com',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Dexter662$blog',
        'USER': 'Dexter662',
        'PASSWORD': '3nf4rm1t4r34',
        'HOST': 'Dexter662.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'