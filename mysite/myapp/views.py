from django.views import generic
from .models import Recipe

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_recipes'

    def get_queryset(self):
        return Recipe.objects.all()

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'detail.html'