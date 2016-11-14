from django.conf.urls import url

from .views import PostListView, PostDetailView, AuthorPostList

urlpatterns = [
    url(r'^posts/([\w-]+)/$', AuthorPostList.as_view(), name="posts_by_author"),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name="post_detail"),
    url(r'^', PostListView.as_view(), name="post_list"),
]
