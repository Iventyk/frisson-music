from django.test import TestCase
from django.urls import reverse

from frisson_music.models import Album


class TestMediaViews(TestCase):

    def test_media_list_returns_unique_media(self):
        Album.objects.create(
            album_title="OST 1",
            media_title="Attack on Titan",
            media_type="ANIME",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21",
        )
        Album.objects.create(
            album_title="OST 2",
            media_title="Attack on Titan",
            media_type="ANIME",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21",
        )

        response = self.client.get(reverse("media-list"))
        self.assertEqual(response.status_code, 200)

        media_list = response.context["media_list"]
        self.assertEqual(len(media_list), 1)

    def test_media_detail_filters_by_media_title(self):
        Album.objects.create(
            album_title="S1",
            media_title="AOT",
            media_type="ANIME",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21",
        )
        Album.objects.create(
            album_title="Movie OST",
            media_title="Other",
            media_type="MOVIE",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21",
        )

        response = self.client.get(reverse("media-detail", args=["AOT"]))
        self.assertEqual(response.status_code, 200)

        albums = response.context["albums"]
        self.assertEqual(albums.count(), 1)
        self.assertEqual(albums.first().media_title, "AOT")
