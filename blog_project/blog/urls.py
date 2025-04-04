from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = (
    # user profile
    path('login/', TokenObtainPairView.as_view(), name = 'login'),
    path('token_refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('profile/', views.UserProfileView.as_view(), name='profile'),
     #User authentication
    path("register/", views.RegisterView.as_view(), name="register"),
    #path("login/", views.LoginView.as_view(), name="login"),
    path('delete/', views.DeleteUserView.as_view(), name = 'delete_user'),
    path('update/', views.UpdateProfileView.as_view(), name = 'update_profile'),

    # #Post CRUD operation
    # path("posts/", views.PostListCreateView.as_view(), name="post_list"),
    # path('posts/<int:pk>/', views.RetrieveUpdateDeleteView.as_view(), name='post-detail'),

    # # Comments Urls view
    # path('comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    # path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

    # # Category Urls View
    # path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    # path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    
)