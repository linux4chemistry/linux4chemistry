# -*- coding: utf-8 -*-
import os, imp

from common import *

# make sure we are running on OpenShift
assert os.environ.has_key('OPENSHIFT_REPO_DIR')

TOP_DIR = os.environ.get('OPENSHIFT_REPO_DIR')
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR')

MEDIA_ROOT = os.path.join(DATA_DIR, 'media/')
STATIC_ROOT = os.path.join(TOP_DIR, 'static/')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'linux4chemistry.sqlite3'),
    }
}

# retrieve more sensitive settings from a dinamically loaded module which is 
# not stored with the sources.
modulefile, pathname, description = imp.find_module('secret', [DATA_DIR,])
secret = imp.load_module('secret', modulefile, pathname, description)

SECRET_KEY = secret.SECRET_KEY
 
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'devel-l4c.rhcloud.com',
    ]

LOGGING['handlers'].update({
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(DATA_DIR, 'l4c.log'),
            },
        })
LOGGING['loggers'].update({
        'django': {
            'handlers': ['logfile'],
            'level': 'WARNING',
            'propagate': False,
            },
        })
