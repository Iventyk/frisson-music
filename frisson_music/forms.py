from django import forms
from .models import Album


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
