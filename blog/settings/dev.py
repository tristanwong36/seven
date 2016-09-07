from .base import *


SECRET_KEY = 'g&mm7c0e)w$=*ss7p-)$e-8o36@^s)r$2fgim$#u5%j4n=a)^!'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHE_MIDDLEWARE_ALIAS = 'default'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




