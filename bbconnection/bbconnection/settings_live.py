"""
Django settings for bbconnection project.

Generated by 'django-admin startproject' using Django 1.11.

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
SECRET_KEY = '*3rg#c!#mwt0jk-e#y%1w!l#8%%dr#@uf*6er9m35f)n4ev5p#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_TITLE = 'bbconnection'

ANONYMOUS_USER_ID = -1
AUTH_USER_MODEL = "auth.User"

LOGIN_URL = "/login/"
LOGIN_URL_BILLING = "/login/"

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    #
    'crispy_forms',
    'datetimewidget',
    'django_tables2',
    'bootstrap3',
    'avatar',
    'annoying',
    'simple_history',
    'widget_tweaks',
    'mptt',
    'django_select2',
    #
    'bbconnlab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'bbconnection.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bbconnection.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'bbconn',
        'USER': 'root',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'localhost',
        'PORT': '3306',
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

LANGUAGE_CODE = 'id'

TIME_ZONE = 'Asia/Jakarta'

DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

AVATAR_AUTO_GENERATE_SIZES = (60,)
AVATAR_PROVIDERS = (
    'avatar.providers.PrimaryAvatarProvider',
    #'avatar.providers.GravatarAvatarProvider',
    'avatar.providers.DefaultAvatarProvider',
)
AVATAR_DEFAULT_URL = 'http://192.168.30.40/media/avatars/admin/avatar.jpg'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

CRISPY_TEMPLATE_PACK="bootstrap3"

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'D:\\BBCONN\\static',
]

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = 'D:\\BBCONN\\media'
MEDIA_URL = '/media/'


#########################
# CIREMAI CONFIGURATION #
#########################

LANGUAGES = (
    ('en', 'English'),
    ('id', 'Indonesia'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# HL7 Message
HL7_ORDER_DIR = 'C:\\HL7'

# report file
RESULT_REPORT_FILE_HEADER = 'D:\\BBCONNREPORT\\report_jrxml\\ciremaiHeader.jrxml'
RESULT_REPORT_FILE_MAIN = 'D:\\BBCONNREPORT\\report_jrxml\\ciremaiReport.jrxml'
RESULT_REPORT_FILE_FOOTER = 'D:\\BBCONNREPORT\\report_jrxml\\ciremaiFooter.jrxml'
RESULT_REPORT_FILE = 'D:\\BBCONNREPORT\\report_jrxml\\ciremaiReport.jasper'
RESULT_REPORT_DIR = 'D:\\BBCONNREPORT\\report_jrxml'

REPORT_DIR = 'D:\\BBCONNREPORT\\report_jrxml\\out'
# Jasper Report Database
JASPER_CONN = {
        'driver': 'mysql',
        'username': 'root',
        'password': 'P@ssw0rd',
        'host': '127.0.0.1',
        'database': 'bbconn'
    }

#########################
