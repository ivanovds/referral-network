"""
WSGI config for referral_network referral_network.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'referral_network.settings')

application = get_wsgi_application()
