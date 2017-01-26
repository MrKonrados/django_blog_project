from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView
from django.views.generic import FormView
from django.views import View
from django.urls import reverse

from .models import Post, Author, Comment
from .forms import CommentForm

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

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostCommentView(SingleObjectMixin, FormView):
    template_name = 'blog/post_detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(PostCommentView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.save()
        return super(PostCommentView, self).form_valid(form)


class PostDetail(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentView.as_view()
        return view(request, *args, **kwargs)

class PostCreate(CreateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = ['title', 'author', 'content']