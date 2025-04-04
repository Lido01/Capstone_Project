from django.urls import path
from . import views

urlpatterns = (
 # Comments Urls view
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

)