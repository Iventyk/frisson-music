from django.views.generic import ListView, DetailView
from .models import Album


class AlbumListView(ListView):
    model = Album
    context_object_name = "albums"
    ordering = ["-release_date"]
    paginate_by = 32


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = "album"
