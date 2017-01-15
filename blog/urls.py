from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', PostListView.as_view(), name="post_list"),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name="post_detail"),
    url(r'^(?P<user>[\w-]+)/posts/$', PostListView.as_view(), name="posts_by_author"),
    url(r'^tag/(?P<tag>[\w-]+)/$', PostListView.as_view(), name="posts_by_tag"),

    # url(r'^posts/create/$', PostCreate.as_view(), name="post_create"),
]
