from django.urls import path, include
from . import views

urlpatterns = (

     #User authentication
    path("register/", views.RegisterView.as_view(), name="login"),
    path("login/", views.LoginView.as_view(), name="login"),

    #Post CRUD operation
    path("posts/", views.PostListCreateView.as_view(), name="post_list"),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # Comments Urls view
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

    # Category Urls View
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    
)