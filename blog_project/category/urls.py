from django.urls import path
from . import views

urlpatterns = (


    # Category Urls View
    path('categories/', views.CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', views.CategoryDetailUpdateDeleteView.as_view(), name='category_detail'),
)