from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed




# #Posts create and list
class PostListView(generics.ListAPIView):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter] #Searching and Orderring
    search_fields = ["title", "content"]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Set the user to the current user



class PostListCreateView(generics.ListCreateAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]  # Enforce authentication
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]  # Searching and Ordering
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise AuthenticationFailed('You need to be authenticated to create posts.')
        serializer.save(user=self.request.user)



# You can detail,delete and update by post_id
class RetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]