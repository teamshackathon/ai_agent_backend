from datetime import timedelta

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = [
    'content-type',
    'access-control-allow-origin',
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'manabiyaai_development',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    # 認証が必要
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    # JWT認証
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}

SIMPLE_JWT = {
    # アクセストークン(1時間)
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    # リフレッシュトークン(3日)
    'REFRESH_TOKEN_LIFETIE': timedelta(days=3),
    # 認証タイプ
    'AUTH_HEADER_TYPES': ('JWT', ),
    # 認証トークン
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', )
}