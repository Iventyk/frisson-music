from django.db import models
from django.urls import reverse


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

