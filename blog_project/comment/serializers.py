from rest_framework import serializers
from .models import Comment
from blog.serializers import UserProfileSerializer
from post.serializers import PostSerializer
from post.models import Post

class CommentSerializer(serializers.ModelSerializer):
    #user = UserProfileSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    user = serializers.SerializerMethodField()
    #post = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ["post", "user", "content", "created_at"]
        read_only_fields = ['user', 'created_at', 'updated_at']

    # def get_post(self, obj):
    #     return str(obj.post.content)
    def get_user(self, obj):
        return str(obj.user.username)
    