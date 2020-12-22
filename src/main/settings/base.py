"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from corsheaders.defaults import default_methods, default_headers
from django.contrib.admin import AdminSite

from common.utils import Config

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
CONFIG_FILE = os.path.join(BASE_DIR, '..', 'config.yml')
config = Config(CONFIG_FILE)

AdminSite.site_title = config.get('SITE_TITLE', 'Django Template Project')
AdminSite.site_header = config.get('SITE_HEADER', 'Django Template Project')
AdminSite.index_title = config.get('INDEX_TITLE', 'Django Template Administration')
SECRET_KEY = config.get('SECRET_KEY', raise_error=True)
DEBUG = config.get('DEBUG', False, cast=bool)
ALLOWED_HOSTS = config.get('ALLOWED_HOSTS', cast=list)

INSTALLED_APPS = [
    'administration',
    'common',

    'rest_framework',
    'drf_yasg',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + ('mysql' if config.get('USE_MYSQL', default=False, cast=bool) else 'postgresql'),
        'NAME': config.get('DB_NAME', raise_error=True),
        'USER': config.get('DB_USER', default='root'),
        'PASSWORD': config.get('DB_PASSWORD', default='toor'),
        'HOST': config.get('DB_HOST', default='127.0.0.1'),
        'PORT': config.get('DB_PORT', default='5432', cast=int)
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'administration.User'

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Bucharest'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#######################################
# CORS CONFIGS
CORS_ORIGIN_WHITELIST = config.get('CORS_ORIGIN_WHITELIST', default='http://localhost:4200', cast=tuple)
CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADERS = default_headers

#######################################
# THUMBNAIL CONFIGS
ADMIN_THUMBNAIL_STYLE = {'display': 'block', 'width': f"{config.get('THUMBNAIL_SIZE', default='200')}px", 'height': 'auto'}
ADMIN_THUMBNAIL_BACKGROUND_STYLE = {'background': '#808080'}
