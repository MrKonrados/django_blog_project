from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Post, Author

class PostListView(ListView):
    paginate_by = 2


    def get_queryset(self):
        if ("user" in self.kwargs):
            # get posts by author
            author = get_object_or_404(Author, username=self.kwargs['user'])
            return Post.objects.filter(author=author).order_by("-modified")
        elif ("tag" in self.kwargs):
            # get posts by tag
            return Post.objects.filter(tags__name__in=[self.kwargs['tag']]).order_by("-modified")
        else:
            return Post.objects.order_by('-modified')


class PostDetailView(DetailView):
    model = Post


class PostCreate(CreateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = ['title', 'author', 'content']


class PostEditView():
    pass


class PostDeleteView():
    pass
