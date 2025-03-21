from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [ "username", "email", "profile_picture"]
    ordering = ["pk"]
admin.site.register(CustomUser, CustomUserAdmin)

