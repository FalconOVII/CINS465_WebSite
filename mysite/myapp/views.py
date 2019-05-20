from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Recipe
from .forms import UserForm

from django.utils.safestring import mark_safe
import json

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
    fields = ['recipe_title', 'category', 'description', 'ingredients', 'instructions', 'alcohol_percentage', 'recipe_logo']
    template_name = 'recipe_form.html'

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipe_title', 'category', 'description', 'recipe_logo']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('myapp:index')

#class Chat(generic.DetailView):
#    template_name = "chat.html"

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('myapp:index')
        
        return render(request, self.template_name, {'form': form})

def chatform(request):
    return render(request, 'chatform.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })