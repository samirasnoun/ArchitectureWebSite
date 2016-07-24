# -*- coding: utf8 -*-
"""

Django settings for archi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

""" 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR =  os.path.dirname(os.path.dirname(__file__))

print BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'svuv+qdakre+p5wp4q9tv98pp&e0k0yy)z8(_47&(1o18+aud7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'website', 
    'localflavor',
    'gunicorn',
     'tinymce',
#    'debug_toolbar',
#    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'archi.urls'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
WSGI_APPLICATION = 'archi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


"""
        'default':{
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'ecomstore',
         'USER': 'ecomstoreuser', 
         'PASSWORD': 'ecomstoreuser',
         'DATABASE_HOST': 'localhost',
         'DATABASE_PORT': '3306',
     }

         'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'd8mch8abq3i2a7',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'eembjbgkusyjay',
            'PASSWORD': 'liWRAKyEP1vBESJqlrogzh3ukn',
            'HOST': 'ec2-54-163-227-94.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }


"""


DATABASES = {


    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }




        # Gandi database
        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #     'NAME': 'postgres',                      # Or path to database file if using sqlite3.
        #     # The following settings are not used with sqlite3:
        #     'USER': 'amar',
        #     'PASSWORD': 'amarlounas',
        #     'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        #     'PORT': '5432',                      # Set to empty string for default.
        # }



}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_URL = '/media/'
STATIC_URL = '/fonts/'
STATIC_ROOT = 'static'
#STATIC_URL = '/media/'
#
#Dev
STATIC_ROOT = '/home/samir/workspace/django/django_site_articles/archi/website/static/'
MEDIA_ROOT = '/home/samir/workspace/django/django_site_articles/archi/website/media/photos/projets/'

#integ
#STATIC_ROOT = '/var/www/media/static'
#MEDIA_ROOT = '/var/www/media/'

#Prod
#STATIC_ROOT = '/srv/data/web/vhosts/default/media/'


STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "website", "media" ),
    #os.path.join(BASE_DIR, "website", "static" ),
    os.path.join(BASE_DIR, "website", "media" , "photos", "projets"),
    os.path.join(BASE_DIR, "website", "media" , "photos", "profil"),
    os.path.join(BASE_DIR, "website", "static" , "css"),
    os.path.join(BASE_DIR, "website", "static" , "js"),
    os.path.join(BASE_DIR, "website", "static" , "fonts"),
)



TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', 
        (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ),
)


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'setisamir2@gmail.com'
EMAIL_HOST_PASSWORD = '15011982!z'
DEFAULT_FROM_EMAIL = 'setisamir2@gmail.com'
DEFAULT_TO_EMAIL = 'samir.asnoun@gmail.com'

ADMINS=(('Samir admin 1', 'samir.asnoun@gmail.com'), ('Samir admin 2', 'setisamir2@gmail.com'))
MANAGERS=(('Samir Manager 1', 'setisamir@gmail.com'), ('Samir Manager 2', 'setisamir3@gmail.com'))

#setisamir2 / milmilouloagh+sin immzwoura An i eole 