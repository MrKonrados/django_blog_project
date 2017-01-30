from django import template

from blog.models import Category, Post

register = template.Library()


@register.inclusion_tag("blog/category_list.html")
def category_list():
    return {'categories': Category.objects.all()}


@register.inclusion_tag("blog/recent_posts.html")
def recent_posts():
    return {'recent_posts': Post.objects.all().order_by("-modified")[:3]}
