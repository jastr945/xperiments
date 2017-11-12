"""
WSGI config for search_engine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "search_engine.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root='/staticfiles', prefix='static/', autorefresh=True)
application.add_files('/searchmedia', prefix='media/')
