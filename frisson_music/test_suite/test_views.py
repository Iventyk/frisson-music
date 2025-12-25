import pytest

from django.urls import reverse
from frisson_music.models import Album


@pytest.mark.django_db
def test_media_list_returns_unique_media(client):
    Album.objects.create(
        album_title="OST 1",
        media_title="Attack on Titan",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )
    Album.objects.create(
        album_title="OST 2",
        media_title="Attack on Titan",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )

    response = client.get(reverse("media-list"))

    media_list = response.context["media_list"]
    assert len(media_list) == 1


@pytest.mark.django_db
def test_media_detail_filters_by_media_title(client):
    Album.objects.create(
        album_title="S1",
        media_title="AOT",
        media_type="ANIME",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )
    Album.objects.create(
        album_title="Movie OST",
        media_title="Other",
        media_type="MOVIE",
        total_tracks=10,
        part_or_season="1",
        release_date="2025-12-21"
    )

    response = client.get(reverse("media-detail", args=["AOT"]))

    albums = response.context["albums"]
    assert albums.count() == 1
    assert albums.first().media_title == "AOT"
