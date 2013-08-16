"""
WSGI config for odin project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import sys

import os


venv_path = os.path.normpath("/opt/venvs/jeffbean") if not 'VIRTUAL_ENV' in os.environ else os.getenv('VIRTUAL_ENV')
if os.path.isdir(venv_path):
    activate_this = os.path.normpath(os.path.join(venv_path, "bin/activate_this.py"))
    execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jbean.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = "jbean.settings"

sys.path.append(os.path.normpath('/opt/web/jeffbean'))

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
