"""
Django settings for kubebooks project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from socket import gethostname, gethostbyname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'k)b&hy@rl69deygl#iizpuizu+$arsr&-&9bp&6el$0v2*6)t(')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booksapp',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kubebooks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kubebooks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRESQL_DB', 'postgres'),
        'USER': os.environ.get('POSTGRESQL_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD', 'mysecretpassword'),
        'HOST': os.environ.get('POSTGRESQL_HOST', 'postgres'),
        'PORT': os.environ.get('POSTGRESQL_PORT', 5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_DIR = [
    os.path.join(BASE_DIR, 'kubebooks', 'static')
]

STATIC_URL = '/static/'

STATIC_ROOT = '/staticfiles'

# Auth0 configurations

SOCIAL_AUTH_TRAILING_SLASH = False                    # Remove end slash from routes

SOCIAL_AUTH_AUTH0_DOMAIN = 'wishlist945.auth0.com'

SOCIAL_AUTH_AUTH0_KEY = os.environ.get('DJANGO_AUTH0_KEY', 'fRPda7JlaXetpi8DFQ6w6TkMsSYjvvqB')

SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('DJANGO_AUTH0_SECRET', 'ZvgWI5Z7FsCcvBhUx2lyFQgMc4Qg1t7pSGt_Vx-bG76K-zn4X7-cag05idwccA7B')

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile'
]

AUTHENTICATION_BACKENDS = {
    'booksapp.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = "/login/auth0"

LOGIN_REDIRECT_URL = "/dashboard"

LOGOUT_REDIRECT_URL = "/authorize"
