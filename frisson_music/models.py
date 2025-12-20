from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Album(models.Model):
    class MediaType(models.TextChoices):
        ANIME = "ANIME", "Anime"
        SERIES = "SERIES", "Series"
        GAME = "GAME", "Game"
        MOVIE = "MOVIE", "Movie"

    media_type = models.CharField(max_length=10, choices=MediaType.choices)
    media_title = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    cover_image_url = models.URLField()
    part_or_season = models.CharField(max_length=255, default="Unknown")
    release_date = models.CharField(max_length=10, default="Unknown")
    artists = models.TextField(help_text="Comma-separated list of artists")
    tracklist = models.TextField(help_text="Each track on a new line")
    total_tracks = models.PositiveIntegerField()
    spotify_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("frisson_music:album-detail", kwargs={"pk": self.pk})


class Rating(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="ratings"
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "album")


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
