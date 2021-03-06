"""
WSGI config for controle_gastos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application
import whitenoise.django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_gastos.settings')

application = get_wsgi_application()
