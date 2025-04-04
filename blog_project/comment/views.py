from django.shortcuts import render
from .models import Comment
from rest_framework import generics
from .serializers import CommentSerializer

# Create your views here.
#Comment create and list for specific post
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
