import os

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# directory to file manage.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      #sciezka absolutna do pliku manage.py

env = environ.Env(
    #defaul types and values
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
# .env is in parent directory to 'settings.py'
# env_file= os.path.join(BASE_DIR, '.env')     #sciezka absolutna do pliku env
# read from .env file if it exists
# environ.Env.read_env(env_file)     #laduje zmienne z pliku env do naszego srodowiska

# DEBUG = env('DEBUG')
# SECRET_KEY = env('SECRET_KEY')
# ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',            # bardzo wazne, zeby to bylo za staticfiles!
    'django_extensions',
    'sass_processor',
    'compressor',
    # 'taggit',
    'reservation.apps.ReservationConfig',
    'homepage.apps.HomepageConfig',
    'menu.apps.MenuConfig',
    'blog.apps.BlogConfig',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',      # <---- to tez dopisujemy na samej gorze to doinsatalowaniu paczek
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurant.urls'

INTERNAL_IPS = [
    '127.0.0.1', 
]

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

WSGI_APPLICATION = 'restaurant.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # zamieniamy dla heroku tak jak ponizej:
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_FINDERS = [         
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
    
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SASS_PROCESOR_ROOT = STATIC_ROOT
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static'),
]

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'