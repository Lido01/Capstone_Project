from .models import CustomUser, Post, Comment
from rest_framework import serializers

class 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "created_at"]

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)#Nested with Post

    class Meta:
        model = Post
        fields = ["title","content", "created_at", "updated_at", "comment"]