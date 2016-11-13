from django.views.generic.list import ListView

from .models import Post


class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        return context

        # TODO: CRUD, Widok szczegółowy postu
