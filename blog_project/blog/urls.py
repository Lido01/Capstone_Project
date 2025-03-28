from django.urls import path, include
from .views import register, login, home, PostListView, PostDetailView

urlpatterns = (
    path("register/", register, name="register"),
    path("login/", login, name="login" ),
    path("home/", home, name="home"),

    #Post CRUD operation
    path("post/list/", PostListView.as_view(), name="post_list"),
    path("post/detail/", PostDetailView.as_view(), name="post_detail"),
)
