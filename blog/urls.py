from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', PostListView.as_view(), name="post_list"),
    url(r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^author/(?P<user>[\w-]+)/$', PostListView.as_view(), name="posts_by_author"),
    url(r'^tag/(?P<tag>[\w-]+)/$', PostListView.as_view(), name="posts_by_tag"),
    url(r'^category/(?P<category>[\w-]+)/$', PostListView.as_view(), name="posts_by_category"),

    # url(r'^posts/create/$', PostCreate.as_view(), name="post_create"),
]
