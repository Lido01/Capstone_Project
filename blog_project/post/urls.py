from django.urls import path
from . import views

urlpatterns = (
    #Post CRUD operation
    path("list/", views.PostListView.as_view(), name="post_list"),
    path("posts/", views.PostListCreateView.as_view(), name="post_list"),
    path('posts/<int:pk>/', views.RetrieveUpdateDeleteView.as_view(), name='post_detail'),
)