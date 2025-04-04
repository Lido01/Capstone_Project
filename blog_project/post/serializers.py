from rest_framework import serializers
from .models import Post
from rest_framework.serializers import SerializerMethodField, ModelSerializer
from comment.models import Comment
from category.models import Category

class PostSerializer(serializers.ModelSerializer):
    user = SerializerMethodField() # To get username in field
    category =  SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["user","title","content", "created_at", "category", "comments"]
    def get_user(self, obj):
        return str(obj.user.username)
    def get_category(self, obj):
        #return str(obj.category.name)
        return str(obj.category.name) if obj.category else "No Category"

    def get_comments(self, obj):
        # Retrieve only the 'content' field of related comments
        return [comment.content for comment in obj.comments.all()]
    def create(self, validated_data):
        # Extract comments data from validated data
        comments_data = validated_data.pop('comments', [])
        post = Post.objects.create(**validated_data)
        # Create comments
        for comment_data in comments_data:
            Comment.objects.create(post=post, **comment_data)
        return post
    
