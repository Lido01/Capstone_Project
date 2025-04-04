from django.db import models
from post.models import Post
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
#4 Creating Comment part to comment for each post
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'