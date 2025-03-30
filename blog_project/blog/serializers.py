from .models import Post, Comment
from rest_framework import serializers 
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email", 'password1', "password2"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'password']

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            password=validated_data['password']
        )
        # Generate an authentication token for the new user
        # Token.objects.create(user=user)
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Envalid Credentials you inserted")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "created_at"]

class PostSerializer(serializers.ModelSerializer):
    #comment = CommentSerializer(many=True, read_only=True)#Nested with Post
    class Meta:
        model = Post
        fields = ["title","content", "created_at", "updated_at"]
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content"]