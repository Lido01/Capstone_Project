from django.urls import path
from . import views

urlpatterns = (


    # Category Urls View
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
)