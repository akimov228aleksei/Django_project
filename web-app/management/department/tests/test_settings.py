"""These settings are used when running tests locally"""
from management.settings import *

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
