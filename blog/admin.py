from django.contrib import admin
from .models import Post, Author, Page


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
