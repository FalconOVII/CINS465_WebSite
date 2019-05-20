# chat/urls.py
from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [
    url(r'^$', views.chatform, name='chatform'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]