from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, User


class PostListView(ListView):
    queryset = Post.objects.order_by('-modified')
    # TODO: Link do postów autora


class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'post'


class AuthorPostList(ListView):
    template_name = 'blog/posts_by_author.html'
    context_object_name = 'author_posts'

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.args[0])
        return Post.objects.filter(author=self.author)
