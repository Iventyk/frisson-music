import pytest

from django.contrib.auth import get_user_model
from frisson_music.models import Album, Rating


User = get_user_model()


@pytest.mark.django_db
def test_user_can_rate_album_once():
    user = User.objects.create_user(username="testuser", password="12345")
    album = Album.objects.create(
        album_title="OST",
        media_title="Media",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )

    Rating.objects.create(user=user, album=album, score=4)

    Rating.objects.update_or_create(
        user=user,
        album=album,
        defaults={"score": 2}
    )

    ratings = Rating.objects.filter(user=user, album=album)
    assert ratings.count() == 1
    assert ratings.first().score == 2


@pytest.mark.django_db
def test_average_rating_calculation():
    user1 = User.objects.create_user(
        username="user1",
        email="user1@example.com",
        password="12345")
    user2 = User.objects.create_user(
        username="user2",
        email="user2@example.com",
        password="12345")

    album = Album.objects.create(
        album_title="OST",
        media_title="Media",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )

    Rating.objects.create(user=user1, album=album, score=4)
    Rating.objects.create(user=user2, album=album, score=2)

    ratings = album.ratings.all()
    avg = sum(r.score for r in ratings) / ratings.count()

    assert avg == 3
