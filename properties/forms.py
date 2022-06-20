from dataclasses import fields
from django import forms
from .models import  House, PropertiesEmail, Search, contactMe


        # tạo ra 1 form hiện ra dựa vào các trường từ model, bản chất các truwownfg là hư nhau để lưu trữ dữ liệu
class PropertiesForm(forms.ModelForm):#kế thừa từ modelForm
    class Meta:
        model = PropertiesEmail # nằm trong model
        fields = ["Email"]   #lấy ra các trường thông tin muốn sử dụng.  trùng với trường models 

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ["UserSearch"]


        
class contactMe_Form(forms.ModelForm):
    class Meta:
        model = contactMe
        fields = ["Name","Email","Number","WriteMessage"]
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Your Name*'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Your Email*'}),
            'Number': forms.TextInput(attrs={'placeholder': 'Your Phone*'}),
            'WriteMessage': forms.Textarea(attrs={'placeholder': 'Messages here*'})
        }