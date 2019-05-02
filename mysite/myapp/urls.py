from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    # /myapp/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /myapp/somenumber/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /myapp/recipe/add/
    url(r'^recipe/add/$', views.RecipeCreate.as_view(), name='recipe_add'),
]