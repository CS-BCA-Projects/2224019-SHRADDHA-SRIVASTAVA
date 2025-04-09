"""
Django settings for Hello project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path, os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*r9c4!u!l$i&zai9gqy^iqjns!x@$^ane6yusxhst*-#9cd5hm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'home.apps.HomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'chatbot',
    'questionnaire',
    'myself',
    'period_tracker.apps.PeriodTrackerConfig',
    'mongo_admin',  # Add app config
]

# Login Redirect Fix
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/tracker/'  # After login, go to tracker
LOGOUT_REDIRECT_URL = '/'  # After logout, go to homepage          # Redirect after logout

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hello.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "template")],
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

WSGI_APPLICATION = 'Hello.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

from pymongo import MongoClient

MONGO_URI = "mongodb+srv://shraddhasrivastva0:shraddha2003" \
"@cluster0.xql6jwb.mongodb.net"
MONGO_DB_NAME = "stree_sewa_satkar"

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Define collections for each app
MONGO_COLLECTIONS = {
    "contact": db["contact"],
    "user": db["user"],
    "response": db["response"],
    "result": db["result"],
    "profile": db["profile"],
    "period_tracker": db["period_tracker"],
}

GEMINI_API_KEY = "AIzaSyDpzZzwLbg7BhGGhmkZbtMmQdFyjAhedhE"

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# 
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Added manually
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 86400  # 1 day session duration
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Helps with CSRF and cross-site issues
SESSION_SAVE_EVERY_REQUEST = True  # Update session on every request
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session active after browser close

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
# from decouple import config

# TWILIO_SID = config('TWILIO_SID')
# TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
# TWILIO_PHONE = config('TWILIO_PHONE')

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
