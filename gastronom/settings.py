"""
Django settings for gastronom project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0)6wj6q-(r@5$t7g=3%dtc4mpl$x&x$(1h#d&qc5m&3h8c^z^*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django_filters',
    'user_profile',
    'jet',
    'comments.apps.CommentsConfig',
    'notifications',
    'catalog',
    # 'super_inlines',
    'django_celery_results',
    'product.apps.ProductConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'discount',
    'gastronom',
    'cart',
    'tinymce',
    'info',
    'order',
]

# celery setting.
CELERY_CACHE_BACKEND = 'default'
CELERY_RESULT_BACKEND = 'django-db'
USE_QUEUE = True


# django setting.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gastronom.urls'

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

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

WSGI_APPLICATION = 'gastronom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PRODUCT_IMAGE_SIZE = {
    'thumbnail': (150, 150),
    'medium': (300,300),
    'medium_large': (768, 768),
    'large': (1024, 1024)
}
REVIEW_IMAGE_SIZE = 300, 300  # for small image size in review

# e-mail settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# Bot settings
TOKEN = ''
PROXY_URL = ''
CHAT_ID = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {'format': '%(name)-12s %(levelname)-8s %(message)s'},
        'file': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',}
    },
    'handlers': {
        'console': {'level': 'INFO', 'class': 'logging.StreamHandler', 'formatter': 'console'},
        'common-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/common.log'},
        'notifications-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/notifications.log'},
        # 'activities-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/activities.log'},
        # 'analytics-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/analytics.log'},
        'cart-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/cart.log'},
        'catalog-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/catalog.log'},
        'comments-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/comments.log'},
        'discount-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/discount.log'},
        # 'info-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/info.log'},
        # 'loyalty-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/loyalty.log'},
        # 'order-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/order.log'},
        'payment-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/payment.log'},
        'product-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/product.log'},
        # 'shipment-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/shipment.log'},
        'user_profile-file': {'level': 'INFO', 'class': 'logging.FileHandler', 'formatter': 'file', 'filename': 'logs/user_profile.log'}
    },
    'loggers': {
        'django': {'level': 'INFO', 'handlers': ['console', 'common-file']},
        # 'activities': {'level': 'INFO', 'handlers': ['console', 'common-file', 'activities-file']},
        # 'analytics': {'level': 'INFO', 'handlers': ['console', 'common-file', 'analytics-file']},
        'cart': {'level': 'INFO', 'handlers': ['console', 'common-file', 'cart-file']},
        'catalog': {'level': 'INFO', 'handlers': ['console', 'common-file', 'catalog-file']},
        'comments': {'level': 'INFO', 'handlers': ['console', 'common-file', 'comments-file']},
        'discount': {'level': 'INFO', 'handlers': ['console', 'common-file', 'discount-file']},
        # 'info': {'level': 'INFO', 'handlers': ['console', 'common-file', 'info-file']},
        # 'loyalty': {'level': 'INFO', 'handlers': ['console', 'common-file', 'loyalty-file']},
        'notifications': {'level': 'INFO', 'handlers': ['console', 'common-file', 'notifications-file']},
        # 'order': {'level': 'INFO', 'handlers': ['console', 'common-file', 'order-file']},
        'payment': {'level': 'INFO', 'handlers': ['console', 'common-file', 'payment-file']},
        'product': {'level': 'INFO', 'handlers': ['console', 'common-file', 'product-file']},
        # 'shipment': {'level': 'INFO', 'handlers': ['console', 'common-file', 'shipment-file']},
        'user_profile': {'level': 'INFO', 'handlers': ['console', 'common-file', 'user_profile-file']},
    }
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
sentry_sdk.init(
    dsn="https://f623636078ed4cc7add578bbb3462672@o490907.ingest.sentry.io/5555592",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

from .local_settings import *
