from pathlib import Path
from datetime import timedelta
import os
import environ

#### patch for django-graphene
# https://github.com/graphql-python/graphene-django/issues/1284#issuecomment-1019998091
import django
from django.utils.encoding import force_str

django.utils.encoding.force_text = force_str

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['JWT_SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Change depending of env for staging/formation/prod
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['localhost', 'host.docker.internal']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_rest_passwordreset',
    'corsheaders',
    'import_export',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ## see https://academind.com/tutorials/localstorage-vs-cookies-xss, use instead http-only cookie
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    # TODO READ FROM env on ./local
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

GRAPHENE = {
    'SCHEMA': 'app.schema.schema',
    'MIDDLEWARE': [
    ],
}
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=1),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

CSRF_COOKIE_SECURE = False
# CSRF_TRUSTED_ORIGINS = ['http://localhost']

# ALLOWED_HOSTS=['http://localhost:3000']
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = ['http://localhost:3000']

CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://localhost:8088']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://localhost:8088']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "api.User"

# if not INSECURE:
#     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
#         'rest_framework.renderers.JSONRenderer',
#     )
