from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = (
    # user profile
    path('login/', TokenObtainPairView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('delete/', views.DeleteUserView.as_view(), name = 'delete_user'),
    path('update/', views.UpdateProfileView.as_view(), name = 'update_profile'),

)