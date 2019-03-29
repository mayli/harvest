import environ

from .plugins import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

env = environ.Env()
env_path = os.path.join(BASE_DIR, 'django_env')
if os.path.isfile(env_path):
    env.read_env(env_path)

SECRET_KEY = '%&lh=f6$s6k3q+iyxdp58dfr*id&5okd=(66n++icmb!1necsw'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'nginx']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'huey.contrib.djhuey',
    'Harvest',
    'home.apps.HomeConfig',
    'settings.apps.SettingsConfig',
    'monitoring.apps.MonitoringConfig',
    'torrents.apps.TorrentsConfig',
    'trackers.apps.TrackersConfig',
]
INSTALLED_APPS += [plugin.app_config_path for plugin in PLUGINS]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Harvest.urls'

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

WSGI_APPLICATION = 'Harvest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DEFAULT_DB_CONNECTION_STRING = 'sqlite:///db.sqlite3?timeout=30'

DATABASES = {
    'default': env.db('DJANGO_DB', default=DEFAULT_DB_CONNECTION_STRING),
    'control': env.db('DJANGO_DB', default=DEFAULT_DB_CONNECTION_STRING),
}

DATABASES['control']['TEST'] = {
    'MIRROR': 'default',
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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = env.str('DJANGO_TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main': {
            'format': '{levelname} {name} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'main',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': env.str('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

HUEY = {
    'name': 'Harvest',
    'always_eager': False,
    'blocking': True,
    'connection': {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
    },
    'consumer': {
        'workers': 2,
        'worker_type': 'thread',
        'periodic': True,
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
