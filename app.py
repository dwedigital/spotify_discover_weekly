import tekore as tk
from tekore._client.full import Spotify


conf = tk.config_from_file('tekore.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])



spotify = Spotify(user_token)

# Get current Discover Weekly playlist
discover = spotify.playlist("37i9dQZEVXcCIq0aSQPBEl")


new_playlist_tracks = []

# Get tracks from current Discover Weekly playlist and append to holder list
for i in discover.tracks.items:
    new_playlist_tracks.append(i.track.uri)


# create new empty playlist
new_playlist = spotify.playlist_create("davedwards","Discover Weekly x",public=True, description = "Copy of Discover Weekly")

# Add all tracks to new playlist
spotify.playlist_add(new_playlist.id, new_playlist_tracks)