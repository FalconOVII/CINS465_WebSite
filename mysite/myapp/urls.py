from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
]
'''
url = (r'^login/$', login{'template_name': 'account/login.html'})
    url = (r'^logout/$', logout{'template_name': 'account/login.html'})

    path('', views.index, name='home'),
    path('testpage/', views.test_page, name='testpage'),
    path('drink_form/', views.drink_form, name='drink_form'),

    # /recipe/

    # /recipe/1/
'''