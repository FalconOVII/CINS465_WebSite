from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    # /myapp/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /myapp/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /myapp/somenumber/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /myapp/somenumber/
    url(r'^chat/$', views.Chat.as_view(), name='chat'),
    
    # /myapp/recipe/add/
    url(r'^recipe/add/$', views.RecipeCreate.as_view(), name='recipe_add'),
    
    # /myapp/recipe/number/
    url(r'^recipe/(?P<pk>[0-9]+)/$', views.RecipeUpdate.as_view(), name='update_recipe'),

    # /myapp/recipe/number/delete/
    url(r'^recipe/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name='delete_recipe'),
]