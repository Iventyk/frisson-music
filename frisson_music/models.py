from django.db import models


class Album(models.Model):
    class MediaType(models.TextChoices):
        SERIES = "SERIES", "Series"
        MOVIE = "MOVIE", "Movie"
        ANIME = "ANIME", "Anime"
        GAME = "GAME", "Game"

    media_type = models.CharField(max_length=10, choices=MediaType.choices)
    media_title = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    cover_image_url = models.URLField()
    part_or_season = models.PositiveIntegerField()
    release_date = models.DateField()
    artists = models.TextField(help_text="Comma-separated list of artists")
    tracklist = models.TextField(help_text="Each track on a new line")
    total_tracks = models.PositiveIntegerField()
    spotify_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
