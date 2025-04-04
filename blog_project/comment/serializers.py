from rest_framework import serializers
from .models import Comment
from blog.serializers import UserProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["content", "created_at", "user"]
