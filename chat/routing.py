from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('chats/', consumers.ChatConsumer.as_asgi()),
]