from django.conf.urls import url

from .views import PostListView

urlpatterns = [
    url(r'^', PostListView.as_view(), name="post_list"),
    # TODO: Linkowanie do widoku szczegółowego postu
]
