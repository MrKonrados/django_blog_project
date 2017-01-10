from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^menu/$', show_genres),
    url(r'^posts/(?P<slug>[-\w]+)/$', PostDetailView.as_view(model=Post, template_name="blog/post_detail.html"),
        name="post_detail"),
    url(r'^posts/create/$', PostCreate.as_view(), name="post_create"),
    url(r'^posts/([\w-]+)/$', AuthorPostList.as_view(), name="posts_by_author"),
    url(r'^$', PostListView.as_view(), name="post_list"),

]
