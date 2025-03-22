from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Post
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        
    else:
        form = RegistrationForm()
    return render(request, "blog/register.html", {'form': form})
