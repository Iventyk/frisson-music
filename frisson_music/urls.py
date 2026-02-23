from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views import (
    HomePageView,
    AlbumListView,
    AlbumDetailView,
    AlbumUpdateView,
    RegisterView,
    UserUpdateView,
    MediaListView,
    MediaDetailView,
)


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("", HomePageView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("profile/edit/", UserUpdateView.as_view(), name="profile-edit"),
    path("media/", MediaListView.as_view(), name="media-list"),
    path(
        "media/<str:media_title>/",
        MediaDetailView.as_view(),
        name="media-detail",
    ),
    path("albums/", AlbumListView.as_view(), name="album-list"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album-detail"),
    path(
        "album/<int:pk>/update/",
        AlbumUpdateView.as_view(),
        name="album-update",
    ),
    path(
        "albums/<str:album_type>/",
        AlbumListView.as_view(),
        name="album-list-by-type",
    ),
    path(
        "comment/<int:comment_id>/delete/",
        views.delete_comment,
        name="delete-comment",
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="frisson_music/about.html"),
        name="about",
    ),
    path(
        "rules/",
        TemplateView.as_view(template_name="frisson_music/rules.html"),
        name="rules",
    ),
]
