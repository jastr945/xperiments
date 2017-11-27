from search_engine.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qz1h9##hp6f!$s6jnkb)e%$g5am7rln9r&nv)84z5ctz7kii@4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.0.109']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'searchapp',
        'USER': 'polina',
        'PASSWORD': 'babybat666',
        'HOST': 'localhost',
        'PORT': '',
    }
}
