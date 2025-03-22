from django.contrib import admin
from .models import CustomUser,Category, Post, Comment


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [ "username", "email", "profile_picture"]
    ordering = ["pk"]
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)