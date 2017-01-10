from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Post, Author


class PostListView(ListView):
    queryset = Post.objects.order_by('-modified')


class PostDetailView(DetailView):
    model = Post


class AuthorPostList(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        author = get_object_or_404(Author, username=self.args[0])
        return Post.objects.filter(author=author).order_by("-modified")


class PostCreate(CreateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = ['title', 'author', 'content']


class PostEditView():
    pass


class PostDeleteView():
    pass


def show_genres(request):
    return render(request, "blog/navbar.html", {'pages': Page.objects.all()})
