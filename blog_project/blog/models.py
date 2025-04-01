from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

#1. Creating the Custom user and overide the default
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user = self.user_create(email, username, password)
        user.id_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager

#2 Creating the Category model to include each post
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

#3 Creating the Post model to include post data
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts", null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ("-created_at",)

#4 Creating Comment part to comment for each post
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'