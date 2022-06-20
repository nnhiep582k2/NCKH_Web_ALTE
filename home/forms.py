from dataclasses import fields
from django import forms
from .models import IndexSendEmail


class IndexSendForm(forms.ModelForm):
    class Meta:
        model = IndexSendEmail
        fields = ["Email"]