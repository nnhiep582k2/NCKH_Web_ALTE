from dataclasses import fields
from django import forms
from .models import  PropertiesEmail, Search


        
class PropertiesForm(forms.ModelForm):
    class Meta:
        model = PropertiesEmail
        fields = ["Email"]      

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ["UserSearch"]