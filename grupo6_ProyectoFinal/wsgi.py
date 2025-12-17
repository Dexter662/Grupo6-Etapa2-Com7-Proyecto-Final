"""
WSGI config for grupo6_ProyectoFinal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Configuracion local
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grupo6_ProyectoFinal.settings')
# Configuracion de produccion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grupo6_ProyectoFinal.settings.production')
application = get_wsgi_application()

