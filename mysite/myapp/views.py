from django.views.generic import genertic

from . import models
from . import forms

class IndexView(genertic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Recipe.objects.all()

class DetailView(genertic.DetailView):
    model = Recipe
    template_name = 'index.html'

'''
def index(request):
    all_recipes = Recipe.objects.all()
    context = {'all_recipes': all_recipes}
    return render(request, "/index.html/", context)

def registration(requst):
    if requst.method == "POST":
        form = UserCreationForm(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/')
    else:
        form = UserCreationForm()

        args = {'form':form}
        return render(request, 'account/registration_form.html', args)






def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, '')






class UserFormView(View):
    form_class = UserFormView
    template_name = 'registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean (normalized) data
            username = form.clean_data['username']
            password = form.clean_data['password']
            user.password(password)
            user.save()





def test_page(request):
    if request.method == "POST":
        print("POST")
    #initial page load
    if request.method == "GET":
        print("GET")

    #Form Submission
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            new_sugg = models.Suggestion()
            new_sugg.suggestion_field = form_instance.cleaned_data["suggestion_field"]
            new_sugg.save()
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()

    i_list = models.Suggestion.objects.all()
    n_list = []
    for item in i_list:
        n_list += [item.suggestion_field]
    context = {
        "body":"Hello World Template Variable",
        "title":"Title Hello",
        "item_list":n_list,
        "form": form_instance
    }
    return render(request, "testpage.html",context=context)

'''