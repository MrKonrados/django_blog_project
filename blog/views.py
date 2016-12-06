from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, User


class PostListView(ListView):
    queryset = Post.objects.order_by('-modified')


class PostDetailView(DetailView):
    model = Post


class AuthorPostList(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.args[0])
        return Post.objects.filter(author=self.author).order_by("-modified")


class PostCreateView():
    pass


class PostEditView():
    pass


class PostDeleteView():
    pass


class UserListView():
    pass


class UserCreateView():
    pass


class UserEditView():
    pass


class UserDeleteView():
    pass
    # TODO: okno logowania
    # TODO: POSTY: crud
    # TODO: Uzytkownicy: crud
