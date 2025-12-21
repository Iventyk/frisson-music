import pytest

from django.urls import reverse
from frisson_music.models import Album, Comment


@pytest.mark.django_db
def test_anonymous_user_cannot_add_comment(client):
    album = Album.objects.create(
        album_title="OST",
        media_title="Media",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )

    client.post(
        reverse("album-detail", args=[album.pk]),
        {"text": "Hack attempt"}
    )

    assert Comment.objects.count() == 0
