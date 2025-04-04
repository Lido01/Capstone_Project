from django.db import models

#2 Creating the Category model to include each post
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name
