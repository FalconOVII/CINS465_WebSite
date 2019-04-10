from django.contrib.auth.models import User
from django import forms

class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(label='Suggestion', max_length=240)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        feilds = ['username', 'email', 'password']