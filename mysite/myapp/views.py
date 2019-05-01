from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'all_recipes': all_recipes})

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'detail.html', {'recipe': recipe })
'''
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
'''