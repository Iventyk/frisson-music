from django.test import TestCase
from django.urls import reverse

from frisson_music.models import Album


class TestAlbumSearch(TestCase):

    def setUp(self):
        Album.objects.create(
            album_title="Best OST Ever",
            media_title="Test",
            media_type="ANIME",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21",
        )
        Album.objects.create(
            album_title="Random Album",
            media_title="Test",
            media_type="ANIME",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21",
        )

    def test_search_by_album_title(self):
        response = self.client.get(reverse("album-list") + "?search=best")

        self.assertEqual(response.status_code, 200)

        albums = response.context["albums"]
        self.assertEqual(albums.count(), 1)
        self.assertIn("Best", albums.first().album_title)
