from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView

from .forms import AlbumUpdateForm
from .models import Album


class AlbumListView(ListView):
    model = Album
    context_object_name = "albums"
    ordering = ["-release_date"]
    paginate_by = 32

    def get_queryset(self):
        queryset = super().get_queryset()
        album_type = self.kwargs.get("album_type")

        if album_type:
            queryset = queryset.filter(media_type=album_type)

        return queryset


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = "album"


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumUpdateForm

    def get_success_url(self):
        return reverse(
            "album-detail",
            kwargs={"pk": self.object.pk}
        )





