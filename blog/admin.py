from django.contrib import admin
from .models import Post, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
