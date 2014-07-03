"""
WSGI config for aldryn_cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import site

ALLDIRS = ['/var/www/aldry-env/lib/python2.7/site-packages']

# Add each new site-packages directory.
for directory in ALLDIRS:
  site.addsitedir(directory)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aldryn_cms.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
