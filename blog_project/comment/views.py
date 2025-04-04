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


    # def get_queryset(self):
    #     self.kwargs["post_id"]
    #     return Comment.objects.filter(post_id=post_id)
    # def perform_create(self, serializer):
    #     post_id = self.kwargs["post_id"]
    #     serializer.save(post_id=post_id)
    #     return super().perform_create(serializer)
# class CommentCreateView(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)  # Set the user to the current user

