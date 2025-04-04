from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField, ModelSerializer
from django.contrib.auth import get_user_model, authenticate
# from django.utils.translation import gettext_lazy as _

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User( 
            username=validated_data['username'],
            email=validated_data['email'])
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Envalid Credentials you inserted")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UpdateProfileSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only = True, required = True)
    new_password = serializers.CharField(write_only = True, min_length = 8, required = False)
    class Meta:
        model = User
        fields = ['username', 'email', 'current_password', 'new_password']

    def validate(self, data):
        user = self.instance
        if 'new_password' in data and data['new_password']:
            if not user.check_password(data['current_password']):
                raise serializers.ValidationError({'current_password': 'Current password is incorrect.'})    
        return data
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('emil', instance.email)
        instance.username = validated_data.get('username', instance.username)
        if 'new_password' in validated_data and validated_data['new_password']:
            instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
    
    
