from django.urls import path
from .views import AlbumListView, AlbumDetailView


urlpatterns = [
    path("albums/", AlbumListView.as_view(), name="album-list"),
    path("album/<int:pk>/", AlbumDetailView.as_view(),
         name="album-detail"),
]
