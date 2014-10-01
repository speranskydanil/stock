"""
Django settings for stock project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.template import add_to_builtins

add_to_builtins('stock.templatetags.helpers')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'shzxmid=vg-jywkcnr4(v8lt%%^4p*^1t3iv^qt9tvh6vgvn(l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'pipeline',
    'sanitizer',
    'stock',
    'blog'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stock.urls'

WSGI_APPLICATION = 'stock.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '../stock.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stock',
        'USER': 'stock',
        'PASSWORD': 'stockpass',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/stock/static'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
          'css/bootstrap.css',
          'css/summernote.css',
          'css/summernote-bs3.css',
          'css/style.css',
          'blog/css/*.css'
        ),
        'output_filename': 'css/main.css'
    }
}

PIPELINE_JS = {
    'main': {
        'source_filenames': (
          'js/html5shiv.js',
          'js/jquery.js',
          'js/bootstrap.js',
          'js/summernote.js',
          'js/script.js',
          'blog/js/*.js'
        ),
        'output_filename': 'js/main.js',
    }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'stock/templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'stock/static'),
)

LOGIN_URL = '/sign_in'
LOGIN_REDIRECT_URL = '/'

