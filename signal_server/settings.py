"""
Django settings for signal_server project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 's!c24+@++wmf)0k*r9$d@y=^(l@5t6=s5l&hz6mnd8ugoz^an@')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'db 127.0.0.1').split()

# Application definition
INSTALLED_APPS = [
    'signal_server.api.v1.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'cuser',
    'trench',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'signal_server.api.v1.middleware.x_robots_middleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Common middleware settings
APPEND_SLASH = True

# Security middleware settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 3600
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'signal_server.urls'

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

WSGI_APPLICATION = 'signal_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME', 'signal_server'),
        'USER': os.environ.get('DATABASE_USER', 'root'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'sadkjghlwh498jksdghlk4wtywaeuht98434'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'PORT': os.environ.get('DATABASE_PORT', 3306),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'cuser.CUser'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# Rest framework
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/hour',
        'user': '1000/day',
        'preKeyBundle': '3/day'
    },
    # Versioning
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
}

# Only using REST framework, therefore safe
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'signature'
)

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password/reset/confirm{uid}/{token}',
    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'SERIALIZERS': {'user_delete': 'signal_server.api.v1.custom_djoser.serializers.UserDeleteSerializer'}
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', None)
EMAIL_PORT = os.environ.get('EMAIL_PORT', None)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', None)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', None)
EMAIL_TIMEOUT = os.environ.get('EMAIL_TIMEOUT', None)
EMAIL_SSL_KEYFILE = os.environ.get('EMAIL_SSL_KEYFILE', None)
EMAIL_SSL_CERTFILE = os.environ.get('EMAIL_SSL_CERTFILE', None)

# Trench (For 2FA)
TRENCH_AUTH = {
    'FROM_EMAIL': os.environ.get('2FA_FROM_EMAIL', "your@email.com"),
    'BACKUP_CODES_LENGTH': 20,  # keep (quantity * length) under 200
    'CONFIRM_DISABLE_WITH_CODE': True,
    'CONFIRM_BACKUP_CODES_REGENERATION_WITH_CODE': True,
    'ALLOW_BACKUP_CODES_REGENERATION': True,
    'APPLICATION_ISSUER_NAME': os.environ.get('2FA_APPLICATION_NAME', "myApplication"),
    'MFA_METHODS': {
        'email': {
            'VERBOSE_NAME': 'email',
            'VALIDITY_PERIOD': 60 * 10,
            'FIELD': 'email',
            'HANDLER': 'trench.backends.basic_mail.SendMailBackend',
            'SERIALIZER': 'trench.serializers.RequestMFACreateEmailSerializer',
            'SOURCE_FIELD': 'email',
        },
        'app': {
            'VERBOSE_NAME': 'app',
            'VALIDITY_PERIOD': 60 * 10,
            'USES_THIRD_PARTY_CLIENT': True,
            'HANDLER': 'trench.backends.application.ApplicationBackend',
        },
    },
}

# Caching
memcache_settings = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('MEMCACHE_LOCATION', 'mc')
    }
}
local_cache_settings = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}
CACHES = {}
if os.environ.get('MEMCACHE_LOCATION', False):
    CACHES = memcache_settings
else:
    CACHES = local_cache_settings
