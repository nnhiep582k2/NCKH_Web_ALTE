from dataclasses import fields
from django import forms

from .models import FeedBack,contactEmail


class contact_Form(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ["Name","Email","Star","Number","WriteMessage"]
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Enter Your Email'}),
            'Star': forms.TextInput(attrs={'placeholder': 'Enter Stars'}),
            'Number': forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number'}),
            'WriteMessage': forms.Textarea(attrs={'placeholder': 'Enter messages here'})
        }
        
class  contactEmailForm(forms.ModelForm):
    class Meta:
        model =  contactEmail
        fields = ["Email"]
        