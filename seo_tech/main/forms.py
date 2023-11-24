from django import forms
from .models import AskLetter


class AskLetterForm(forms.Form):
    name = forms.CharField()
    mail = forms.EmailField()
    message = forms.CharField(required=False)
