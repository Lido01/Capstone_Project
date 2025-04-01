from .models import Post, Comment, Category
from rest_framework import serializers 
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['id', 'username', 'email']

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']

#     def create(self, validated_data):
#         # Create a new user with a hashed password
#         user = User( 
#             username=validated_data['username'],
#             email=validated_data['email'])
#         user.set_password(validated_data['password'])  # Hash the password
#         user.save()
#         return user

#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError(_("This email is already in use."))
#         return value

#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError(_("This username is already taken."))
#         return value
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError(_("This email is already in use."))
    #     return value

    # def validate_username(self, value):
    #     if User.objects.filter(username=value).exists():
    #         raise serializers.ValidationError(_("This username is already taken."))
    #     return value




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Envalid Credentials you inserted")

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["content", "user", "created_at"]

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)#Nested with Post
    class Meta:
        model = Post
        fields = ["title","content","author", "created_at", "updated_at", "comment"]
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

