import tekore as tk
from tekore._client.full import Spotify
import datetime


def CopyPlaylist(request):

    conf = tk.config_from_file('tekore.cfg', return_refresh=True)
    user_token = tk.refresh_user_token(*conf[:2], conf[3])



    spotify = Spotify(user_token)

    # Get current Discover Weekly playlist
    discover = spotify.playlist("37i9dQZEVXcCIq0aSQPBEl")


    new_playlist_tracks = []

    # Get tracks from current Discover Weekly playlist and append to holder list
    for i in discover.tracks.items:
        new_playlist_tracks.append(i.track.uri)

    today = datetime.date.today()

    year, week_num, day_of_week = today.isocalendar()

    print(year, week_num, day_of_week)

    # create new empty playlist
    new_playlist = spotify.playlist_create("davedwards",f"Discover Weekly {year} wk{week_num-1}",public=True, description = "Copy of Discover Weekly")

    # Add all tracks to new playlist
    spotify.playlist_add(new_playlist.id, new_playlist_tracks)

    return "Created PLaylist"