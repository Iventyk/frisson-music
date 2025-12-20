from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import (
    HomePageView,
    AlbumListView,
    AlbumDetailView,
    AlbumUpdateView,
    RegisterView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("albums/", AlbumListView.as_view(),
         name="album-list"),
    path("album/<int:pk>/", AlbumDetailView.as_view(),
         name="album-detail"),
    path("album/<int:pk>/update/", AlbumUpdateView.as_view(),
         name="album-update"),
    path("albums/<str:album_type>/", AlbumListView.as_view(),
         name="album-list-by-type"),
]
