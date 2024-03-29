# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^/myapp/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]