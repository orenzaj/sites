"""
Django settings for sites project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


def add_new_path(new_path):
    return lambda * x: os.path.join(os.path.abspath(new_path), *x)


BASE_PATH = add_new_path(os.path.dirname(__file__))
ROOT_PATH = add_new_path(BASE_PATH(".."))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hx*4n_7$liw4%wtzyn0h^)%j%-8dv4e6kx42g7gr-xu+w8-k+2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "*",
]

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'bootstrap4',
    'corsheaders',
    'channels',
    'django_extensions',
    'django_react_templatetags',
    'rest_framework',
]
MY_APPS = [
    'apps.rhythm',
    'apps.chat',
    'sites.orenza',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS


DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
THIRD_PARTY_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
# MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE
MIDDLEWARE = THIRD_PARTY_MIDDLEWARE + DJANGO_MIDDLEWARE

ROOT_URLCONF = 'urls'

DJANGO_CONTEXT_PROCESSORS = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]
THIRD_PARTY_CONTEXT_PROCESSORS = [
    'django_react_templatetags.context_processors.react_context_processor',
]
CONTEXT_PROCESSORS = DJANGO_CONTEXT_PROCESSORS + THIRD_PARTY_CONTEXT_PROCESSORS
TEMPLATE_DIRS = [
    ROOT_PATH("frontend"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': CONTEXT_PROCESSORS,
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Channels
ASGI_APPLICATION = 'urls.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                ("localhost", 6379),
            ],
        }
    }
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
pass_validator = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ".".join([pass_validator, 'UserAttributeSimilarityValidator']),
    },
    {
        'NAME': ".".join([pass_validator, 'MinimumLengthValidator']),
    },
    {
        'NAME': ".".join([pass_validator, 'CommonPasswordValidator']),
    },
    {
        'NAME': ".".join([pass_validator, "NumericPasswordValidator"]),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
