from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('testpage', views.test_page, name='testpage'),
]