import os

from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

_SETTINGS_DIR = os.path.dirname(__file__)

TOP_DIR = os.path.normpath(os.path.join(_SETTINGS_DIR, "../../../"))
DATA_DIR = os.path.normpath(os.path.join(TOP_DIR, "../dev-data"))

INSTALLED_APPS += (
    'django.contrib.admin',
)

MEDIA_ROOT = os.path.join(DATA_DIR, 'media/')
STATIC_ROOT = os.path.join(TOP_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'linux4chemistry.sqlite3'),
    }
}

# Make this unique, and don't share it with anybody.
# (the instancesdeployed on openshift expect to find their own in a module
# dynamically loaded from the $OPENSHIFT_DATA_DIR, for the development env
# this is not so important)
SECRET_KEY = '9b3%js#ais(Ew5s&amp;yc3gnv$w^0crncbq)$Ewoawt73qcvir!x7'
ALLOWED_HOSTS = ['*']


