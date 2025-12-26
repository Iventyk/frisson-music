from django.contrib.auth import get_user_model
from django.test import TestCase

from frisson_music.models import Album, Rating


User = get_user_model()


class TestRatings(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="user1@example.com",
            password="12345"
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="user2@example.com",
            password="12345"
        )

        self.album = Album.objects.create(
            album_title="OST",
            media_title="Media",
            media_type="ANIME",
            total_tracks=10,
            part_or_season="1",
            release_date="2025-12-21"
        )

    def test_user_can_rate_album_once(self):
        Rating.objects.create(
            user=self.user1,
            album=self.album,
            score=4
        )

        Rating.objects.update_or_create(
            user=self.user1,
            album=self.album,
            defaults={"score": 2}
        )

        ratings = Rating.objects.filter(
            user=self.user1,
            album=self.album
        )

        self.assertEqual(ratings.count(), 1)
        self.assertEqual(ratings.first().score, 2)

    def test_average_rating_calculation(self):
        Rating.objects.create(
            user=self.user1,
            album=self.album,
            score=4
        )
        Rating.objects.create(
            user=self.user2,
            album=self.album,
            score=2
        )

        ratings = self.album.ratings.all()
        avg_rating = sum(r.score for r in ratings) / ratings.count()

        self.assertEqual(avg_rating, 3)
