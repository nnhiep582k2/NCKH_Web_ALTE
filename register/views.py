import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})