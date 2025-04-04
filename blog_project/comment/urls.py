from django.urls import path
from . import views

urlpatterns = (
 # Comments Urls view
    path('comments/', views.CommentListCreateView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),

)