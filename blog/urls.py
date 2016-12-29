from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name="post_detail"),
    url(r'^posts/create/$', PostCreate.as_view(), name="post_create"),
    url(r'^posts/([\w-]+)/$', AuthorPostList.as_view(), name="posts_by_author"),
    url(r'^$', PostListView.as_view(), name="post_list"),
]
