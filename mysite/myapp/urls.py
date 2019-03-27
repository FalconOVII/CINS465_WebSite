from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('page_view', views.page_view, name='page_view'),
]
