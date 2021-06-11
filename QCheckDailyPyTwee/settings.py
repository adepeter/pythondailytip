"""Django settings for QCheckDailyPyTwee project.Generated by 'django-admin startproject' using Django 3.2.4.For more information on this file, seehttps://docs.djangoproject.com/en/3.2/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/3.2/ref/settings/"""import osfrom pathlib import Path, PurePathfrom django.urls import reverse_lazyimport django_herokuimport dj_database_urlfrom decouple import config# Build paths inside the project like this: BASE_DIR / 'subdir'.BASE_DIR = Path(__file__).resolve().parent.parent# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = config('SECRET_KEY')# SECURITY WARNING: don't run with debug turned on in production!DEBUG = config('DEBUG', default=False, cast=bool)sALLOWED_HOSTS = ['pythontips247.herokuapp.com']# Application definitionINSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    # 3rd party libraries    'django_apscheduler',    'rest_framework',    # QuickCheckDailyPyTwee apps    'apps.restapi.apps.RestAPIConfig',    'apps.twee.apps.TweeConfig',]MIDDLEWARE = [    # 'whitenoise.middleware.WhiteNoiseMiddleware',    'django.middleware.security.SecurityMiddleware',    'django.contrib.sessions.middleware.SessionMiddleware',    'django.middleware.common.CommonMiddleware',    'django.middleware.csrf.CsrfViewMiddleware',    'django.contrib.auth.middleware.AuthenticationMiddleware',    'django.contrib.messages.middleware.MessageMiddleware',    'django.middleware.clickjacking.XFrameOptionsMiddleware',]ROOT_URLCONF = 'QCheckDailyPyTwee.urls'TEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [BASE_DIR / 'templates']        ,        'APP_DIRS': True,        'OPTIONS': {            'context_processors': [                'django.template.context_processors.debug',                'django.template.context_processors.request',                'django.contrib.auth.context_processors.auth',                'django.contrib.messages.context_processors.messages',            ],        },    },]WSGI_APPLICATION = 'QCheckDailyPyTwee.wsgi.application'# Database# https://docs.djangoproject.com/en/3.2/ref/settings/#databasesDATABASES = {    'default': dj_database_url.config(        default=config('DATABASE_URL'), conn_max_age=600, ssl_require=True    )}# Password validation# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },]# Internationalization# https://docs.djangoproject.com/en/3.2/topics/i18n/LANGUAGE_CODE = 'en-us'TIME_ZONE = 'Africa/Lagos'USE_I18N = TrueUSE_L10N = TrueUSE_TZ = False# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/3.2/howto/static-files/STATIC_URL = '/static/'STATIC_ROOT = BASE_DIR / 'static'STATICFILES_DIRS = [    PurePath(BASE_DIR).joinpath('static')]# Default primary key field type# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-fieldDEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'LOGIN_URL = reverse_lazy('tweeapps:users:auth:login')LOGOUT_URL = reverse_lazy('tweeapps:users:auth:logout')LOGOUT_REDIRECT_URL = reverse_lazy('tweeapps:twee:home')LOGIN_REDIRECT_URL = reverse_lazy('tweeapps:twee:home')prod_db  =  dj_database_url.config(conn_max_age=500)DATABASES['default'].update(prod_db)# Activate Django-Heroku.django_heroku.settings(locals())# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'SCHEDULER_CONFIG = {    "apscheduler.jobstores.default": {        "class": "django_apscheduler.jobstores:DjangoJobStore"    },    'apscheduler.executors.processpool': {        "type": "threadpool"    },}SCHEDULER_AUTOSTART = True