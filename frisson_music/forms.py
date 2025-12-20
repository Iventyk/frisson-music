from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Album, User


class AlbumUpdateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "media_type",
            "media_title",
            "album_title",
            "cover_image_url",
            "part_or_season",
            "release_date",
            "artists",
            "tracklist",
            "total_tracks",
            "spotify_url",
        ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
