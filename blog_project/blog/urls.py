from django.urls import path, include
from . import views

urlpatterns = (

     #User authentication
    path("register/", views.RegisterView.as_view(), name="login"),
    path("login/", views.LoginView.as_view(), name="login"),

    #Post CRUD operation
    path("posts/", views.PostListCreateView.as_view(), name="post_list"),
    path("posts/<int:post_id>/comments/", views.CommentListCreateView.as_view(), name="comment_list_create"),
    
)