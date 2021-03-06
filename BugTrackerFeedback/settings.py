"""
Django settings for BugTrackerFeedback project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ceq*f^7wpze91w@b+1r@&o_fxi!8jz%@&0@bhy-mi%4fk2!=e%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Feedback',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'BugTrackerFeedback.urls'

WSGI_APPLICATION = 'BugTrackerFeedback.wsgi.application'

# MEDIA_ROOT = '/BugTrackerFeedback'
# STATIC_ROOT = '/BugTrackerFeedback/static'
# STATICFILES_DIRS = 'C:/Python33/Lib/site-packages/django/contrib/admin/static'
# STATIC_URL = '/BugTrackerFeedback/static'
# ADMIN_MEDIA_PREFIX = '/static/admin/'
TEMPLATE_LOADER = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader')
TEMPLATE_DIRS = (
    "/BugTrackerFeedback/templates/",
    # "/BugTrackerFeedback/Feedback/templates",

)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
