from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
from blog.models import CustomUser

#User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts", null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ("-created_at",)