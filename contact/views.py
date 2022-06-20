import tkinter
from xmlrpc.client import Boolean
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import contact_Form, contactEmailForm
from .models import FeedBack, contactEmail
from tkinter import messagebox
# Create your views here.

class ContactForm(View):
    def get(self , request):
        CF = contact_Form
        CE = contactEmailForm
        return render(request, 'contact/contact.html',{'CF' : CF , 'CE' : CE})
    
    def post(self,request):
        if request.method == "POST":
            CF = contact_Form(request.POST)
            if CF.is_valid():
                CF.save()
                return HttpResponse('FeedBack Success')
        else:
                return HttpResponse('not Post')

def postEmail(request):
    if request.method == "POST":
        EM = contactEmailForm(request.POST)
        if EM.is_valid():
            EM.save()
            return HttpResponse('Send Success')
    else:
        return HttpResponse('not Post')

