import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q%u&ir4%0jw)l(tc$1#qq)0)w%7n)*9v$jj=$$*u@i99*x^(&f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] #TODO DEFINE LIST OF HOSTS WHICH ARE ALLOWED TO DO REQUESTS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'gabinetLaryngologii.blog',
    'corsheaders',
    'gabinetLaryngologii.material',
    'storages',
    'gabinetLaryngologii.contact',
    'gabinetLaryngologii.visit',
]

DEFAULT_FILE_STORAGE = 'gabinetLaryngologii.material.utils.dropbox.DropBoxFileStorageCustom'
DROPBOX_OAUTH2_TOKEN = '9vC0Lf2weJAAAAAAAAAAXQODaH8cHUQyx_6liRV2LIFNWoFPvjPIiUHJMJqU0wyc'
DROPBOX_ROOT_PATH = '/media/'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True #TODO CHANGE TO FLASE WHEN HOSTS WILL BE PROVIDED
ROOT_URLCONF = 'gabinetLaryngologii.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'gabinetLaryngologii.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.config()}

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

LANGUAGE_CODE = 'pl-pl'

DATE_FORMAT = ['d-m-Y']

DATE_INPUT_FORMATS = ['%Y-%m-%d']

TIME_ZONE = 'Europe/Warsaw'

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gabinet.laryngologiczny.gdynia@gmail.com'
EMAIL_HOST_PASSWORD = '!@#$%qazWSX'
#TODO U CAN PARAMETRIZE IT BY ENV VARIABLES

CELERY_BROKER_URL = os.environ.get('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

ENCRYPT_KEY = b'zZQddQyotjrytGwwHiTJeCurAkC5sZ7hCk9GnkAX0LA='

EXPIRATION_TOKEN_TIME = 43200
CONTACT_URL = "https://gabinetlogopedyczny.mglernest.now.sh/contact"
CONFIRMATION_URL = "https://gabinetlogopedyczny.mglernest.now.sh/visits/confitmation/"
