from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag("blog/category_list.html")
def category_list():
    return {'categories': Category.objects.all()}
