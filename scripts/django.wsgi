import os
import sys
path = '/home/bitnami/foursquare-hackathon'

if path not in sys.path:
   sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'foodlister.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()