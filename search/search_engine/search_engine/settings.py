"""
Django settings for search_engine project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qz1h9##hp6f!$s6jnkb)e%$g5am7rln9r&nv)84z5ctz7kii@4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.0.109', 'search.mee.how']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'searchapp',
    'tinymce',
    'django_elasticsearch_dsl',
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

ROOT_URLCONF = 'search_engine.urls'

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

WSGI_APPLICATION = 'search_engine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/search_engine/search_engine',
    }
}

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'elastic:changeme@localhost:9200'
    },
}

ELASTICSEARCH_DSL_INDEX_SETTINGS = {
    'number_of_shards': 1
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

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "table,spellchecker,paste,searchreplace,emotions,autosave,preview,wordcount",
    'menubar': "tools",
    'toolbar': "spellchecker",
    'theme_advanced_buttons3' : "table,spellchecker,paste,searchreplace,emotions,autosave,preview,wordcount",
    'width': 1200,
    'height': 700,
    'font-size': '12px',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

TINYMCE_SPELLCHECKER = True

TINYMCE_COMPRESSOR = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'searchapp', 'static')]

STATIC_ROOT = '/staticfiles'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/searchmedia'
