from django.shortcuts import render, redirect
from django.contrib.auth import login

# import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_user(request):
    return render(request, 'login.html')

def garage(request):
    return render(request, 'garage.html')