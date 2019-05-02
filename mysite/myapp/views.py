from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_recipes'

    def get_queryset(self):
        return Recipe.objects.all()

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'detail.html'

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_title', 'category', 'description', 'recipe_logo']