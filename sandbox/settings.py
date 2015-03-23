import os, hashlib
from fnmatch import fnmatch
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as messages
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, LOGGING, AUTHENTICATION_BACKENDS
from varlet import variable
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

here = lambda *path: os.path.normpath(os.path.join(os.path.dirname(__file__), *path))
ROOT = lambda *path: here("../", *path)

DEBUG = variable("DEBUG", False)
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': variable("DB_NAME", 'sandbox'),
        'USER': variable("DB_USER", 'root'),
        'PASSWORD': variable("DB_PASSWORD", ''),
        'HOST': variable("DB_HOST", 'localhost'),
        'PORT': '',
    }
}

ADMINS = [["ssean1", "seanofthesissons@gmail.com"]]

"""
Continue integrating settings.py with varlet variables;

    Reference:
[MLP](https://github.com/PSU-OIT-ARC/mlp/blob/master/mlp/settings.py)
"""


ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# allow the use of wildcards in the INTERNAL_IPS setting
class IPList(list):
    # do a unix-like glob match
    # E.g. '192.168.1.100' would match '192.*'
    def __contains__(self, ip):
        for ip_pattern in self:
            if fnmatch(ip, ip_pattern):
                return True
        return False

INTERNAL_IPS = IPList(['10.*', '192.168.*'])


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sandbox.dash',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sandbox.urls'

WSGI_APPLICATION = 'sandbox.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = ROOT("static")

STATICFILES_DIRS = (
    here("../", "static"),
)

TMP_ROOT = ROOT("tmp")

TEMPLATE_DIRS = (
    here("templates"),
)

#SECRET_KEY = '6fv((#b5)0ta2_96t!4*jw9qv*!87l$q@&gtr8eok5-%$esz%k'
SECRET_KEY = variable("SECRET_KET", os.urandom(64).decode("latin1"))
