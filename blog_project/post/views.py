from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


#Posts create and list
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter] #Searching and Orderring
    search_fields = ["title", "content"]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the current user

# You can detail,delete and update by post_id
class RetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]