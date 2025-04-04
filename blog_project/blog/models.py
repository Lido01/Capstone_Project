from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

#Custom 
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Email is required")
        # Normalize email and create the user
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        # Use create_user instead of non-existent 'user_create'
        user = self.create_user(username=username, email=email, password=password)
        # Set is_staff and is_superuser attributes to True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)  # Custom email field
    username = models.CharField(max_length=100)  # Custom username field
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile picture
    bio = models.TextField(blank=True, null=True)  # Optional bio field

    USERNAME_FIELD = "email"  # Email will be used for authentication
    REQUIRED_FIELDS = ["username"]  # Username is a required field for superuser creation

    objects = CustomUserManager()  # Assign the custom manager