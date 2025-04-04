from django.urls import path
from . import views

urlpatterns = (
    #Post CRUD operation
    path("posts/", views.PostListCreateView.as_view(), name="post_list"),
    path('posts/<int:pk>/', views.RetrieveUpdateDeleteView.as_view(), name='post_detail'),
)