from django.contrib import admin
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage

from mptt.admin import MPTTModelAdmin

from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

# class FlatPageAdmin(FlatPageAdmin):
#     pass
#
#
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)
