from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from .models import Post
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, PostForm

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

def login(request):
    if request.method =="POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()
    return render(request, "blog/login.html", {"form": form})

def home(request):
    return render(request, "blog/home.html")

#Post CRUD Operation
class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post/post_list.html"
    context_object_name = "posts"
    

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post

class PostDeleteView(generic.DeleteView):
    model = Post
