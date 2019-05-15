from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    template_name = 'recipe_form.html'

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipe_title', 'category', 'description', 'recipe_logo']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('myapp:index')

class Chat(generic.DetailView):
    template_name = "chat.html"