import os
import django
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# --- Django setup ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frisson_music_service.settings")
django.setup()

from frisson_music.models import Album

# --- Spotify setup ---
CLIENT_ID = "747ee443bedf429aade7446a318b7085"
CLIENT_SECRET = "08eef7f7800d47f2a0bb0eff7c8a3645"

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# --- Album search ---
search_queries = ["Evangelion", "Naruto", "Attack on Titan", "DUNE", "DOOM", "Stranger Things"]
max_albums_per_query = 10

for query in search_queries:
    results = sp.search(q=f"album:{query}", type="album", limit=max_albums_per_query)
    albums = results['albums']['items']

    for alb in albums:
        album_title = alb['name']
        cover_image_url = alb['images'][0]['url'] if alb['images'] else ""
        release_date = alb['release_date']
        artists = ", ".join([artist['name'] for artist in alb['artists']])
        total_tracks = alb['total_tracks']
        spotify_url = alb['external_urls']['spotify']

        tracks_data = sp.album_tracks(alb['id'])
        tracklist = "\n".join([track['name'] for track in tracks_data['items']])

        Album.objects.update_or_create(
            album_title=album_title,
            defaults={
                "cover_image_url": cover_image_url,
                "release_date": release_date,
                "artists": artists,
                "tracklist": tracklist,
                "total_tracks": total_tracks,
                "spotify_url": spotify_url
            }
        )

print("Populate complete!")
