"""
WSGI config for urlshortener project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import sys
import os

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, root)
sys.path.append('/usr/local/lib/python2.7/dist-packages')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urlshortener.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
