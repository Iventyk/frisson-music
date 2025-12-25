import pytest
from django.urls import reverse
from frisson_music.models import Album


@pytest.mark.django_db
def test_search_by_album_title(client):
    Album.objects.create(
        album_title="Best OST Ever",
        media_title="Test",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )
    Album.objects.create(
        album_title="Random Album",
        media_title="Test",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )

    response = client.get(reverse("album-list") + "?search=best")

    albums = response.context["albums"]
    assert albums.count() == 1
    assert "Best" in albums.first().album_title
