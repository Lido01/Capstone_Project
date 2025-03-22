from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Post, Comment
from django import forms
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]