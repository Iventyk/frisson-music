import os
import django
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from frisson_music.models import Album


# --- Django setup ---
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "frisson_music_service.settings"
)
django.setup()

# --- Spotify setup ---
CLIENT_ID = "Your_spotify_client_id"
CLIENT_SECRET = "Your_spotify_client_secret"

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)

# --- Album search ---
search_queries = [
    "Evangelion",
    "Naruto",
    "Attack on Titan",
    "DUNE",
    "DOOM",
    "Stranger Things",
]
max_albums_per_query = 10

for query in search_queries:
    results = sp.search(
        q=f"album:{query}", type="album", limit=max_albums_per_query
    )
    albums = results["albums"]["items"]

    for alb in albums:
        album_title = alb["name"]
        cover_image_url = alb["images"][0]["url"] if alb["images"] else ""
        raw_release_date = alb["release_date"]
        artists = ", ".join([artist["name"] for artist in alb["artists"]])
        total_tracks = alb["total_tracks"]
        spotify_url = alb["external_urls"]["spotify"]

        tracks_data = sp.album_tracks(alb["id"])
        tracklist = "\n".join(
            [track["name"] for track in tracks_data["items"]]
        )

        # --- Date Convertion with parse_release_date ---
        release_date, release_date_precision = Album.parse_release_date(
            raw_release_date
        )

        Album.objects.update_or_create(
            album_title=album_title,
            defaults={
                "cover_image_url": cover_image_url,
                "release_date": release_date,
                "release_date_precision": release_date_precision,
                "artists": artists,
                "tracklist": tracklist,
                "total_tracks": total_tracks,
                "spotify_url": spotify_url,
            },
        )

print("Populate complete!")
