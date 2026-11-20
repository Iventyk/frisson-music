from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Album, Comment, Rating


User = get_user_model()


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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Write your comment...",
                }
            )
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["score"]
        widgets = {
            "score": forms.HiddenInput(),
        }
