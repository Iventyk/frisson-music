import pytest
from django.contrib.auth import get_user_model

from frisson_music.models import Album, Rating


User = get_user_model()


@pytest.mark.django_db
def test_user_can_rate_album_once():
    user = User.objects.create_user(
        username="testuser",
        email="user1@example.com",
        password="12345"
    )
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

    rating = Rating.objects.get(user=user, album=album)

    assert Rating.objects.count() == 1
    assert rating.score == 2
