"""
ASGI config for ArceGram project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArceGram.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django
import chat.routing
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack



application = ProtocolTypeRouter({
    'https': get_asgi_application(),
    # 'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
