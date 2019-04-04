from django.shortcuts import render

from . import models
from . import forms

def index(request):
    '''
    if request.method == "POST":
        print("POST")
    #initial page load
    if request.method == "GET":
        print("GET")
    '''
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
    return render(request, "testpage.html", context=context)

def test_page(request):
    return render(request, "testpage.html")