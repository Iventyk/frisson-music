from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg
from django.urls import reverse
from datetime import date


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class AlbumQuerySet(models.QuerySet):
    def latest_by_type(self, media_type, n=5):
        return self.filter(media_type=media_type).order_by("-release_date")[:n]

    def by_media_title(self, media_title, media_type=None):
        qs = self.filter(media_title=media_title)
        if media_type:
            qs = qs.filter(media_type=media_type)
        return qs.order_by("part_or_season", "-release_date")


class Album(models.Model):
    class MediaType(models.TextChoices):
        ANIME = "ANIME", "Anime"
        SERIES = "SERIES", "Series"
        GAME = "GAME", "Game"
        MOVIE = "MOVIE", "Movie"

    class ReleaseDatePrecision(models.TextChoices):
        YEAR = "year", "Year"
        MONTH = "month", "Month"
        DAY = "day", "Day"

    media_type = models.CharField(max_length=10, choices=MediaType.choices)
    media_title = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    cover_image_url = models.URLField()
    part_or_season = models.CharField(max_length=255, default="Unknown")
    release_date = models.DateField(null=True)
    release_date_precision = models.CharField(
        max_length=10,
        choices=ReleaseDatePrecision.choices,
        null=True,
    )
    artists = models.TextField(help_text="Comma-separated list of artists")
    tracklist = models.TextField(help_text="Each track on a new line")
    total_tracks = models.PositiveIntegerField()
    spotify_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AlbumQuerySet.as_manager()

    class Meta:
        indexes = [
            models.Index(fields=["media_title"], name="idx_media_title"),

            GinIndex(
                name="idx_album_title_trgm",
                fields=["album_title"],
                opclasses=["gin_trgm_ops"]
            ),

            models.Index(fields=["release_date"], name="idx_release_date"),
        ]

    def get_absolute_url(self):
        return reverse("frisson_music:album-detail", kwargs={"pk": self.pk})

    @staticmethod
    def parse_release_date(value: str):
        parts = value.split("-")
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 1
        day = int(parts[2]) if len(parts) > 2 else 1

        if len(parts) == 1:
            precision = Album.ReleaseDatePrecision.YEAR
        elif len(parts) == 2:
            precision = Album.ReleaseDatePrecision.MONTH
        else:
            precision = Album.ReleaseDatePrecision.DAY

        return date(year, month, day), precision

    def average_rating(self):
        return self.ratings.aggregate(avg_score=Avg("score"))["avg_score"] or 0


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="ratings")
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "album")


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
