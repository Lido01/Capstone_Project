from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Post, Comment
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email","password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category"]
    def clean(self):
        title = self.cleaned_data("title")
        if len(title) < 3:
            raise forms.ValidationError("The title must be at least 4 characters long")
        return title
