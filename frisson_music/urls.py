from django.urls import path
from .views import AlbumListView, AlbumDetailView, AlbumUpdateView


urlpatterns = [
    path("albums/", AlbumListView.as_view(),
         name="album-list"),
    path("album/<int:pk>/", AlbumDetailView.as_view(),
         name="album-detail"),
    path("album/<int:pk>/update/", AlbumUpdateView.as_view(),
         name="album-update"),
    path("albums/<str:album_type>/", AlbumListView.as_view(),
         name="album-list-by-type"),
]
