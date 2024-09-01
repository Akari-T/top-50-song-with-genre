import spotipy
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
from dotenv import load_dotenv
import csv
import os

load_dotenv()

# Confirmed run!
# The modification would be to get the genre infor from the artist.
# Oh hm should I get the track entries as well or is that redundant.
# It currently doesn't include the track id, making it hard to use for other analyzes.
# Want to add identifier so we can use the data for other analyzes in the future.
def extract_data(playlist_id, country):

    # The csv file storing the top 50
    csv_file_path = './data/test/spotify-streaming-top-50-mod-' + country + '.csv'
    today = datetime.today().strftime('%Y-%m-%d')

    ## Boolean to check if today's top 50 has been recorded or not
    date_processed = False
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # Checks the rows and if top 50 from today is already there, stops
            for row in reader:
                if row['date'] == today:
                    date_processed = True
                    print("Day " + today + " already processed | Country: " + country)
                    break

    # Credentials to access Spotify API
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    if not date_processed:
        # Get all songs from playlist
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        # Extract URIs of all songs composing the playlist
        uris = [track['track']['uri'] for track in tracks]

        # Obtaining tracks data and sorting it by field popularity (indicator of streaming count)
        ## sorted_tracks = sorted(uris, key=lambda uri: sp.track(uri)['popularity'], reverse=True)

        # Creating list of lists and including the header of the final CSV file
        spotify_data = []
        head = ['date', 'position', 'song', 'artist', 'popularity', 'duration_ms', 'album_type', 'total_tracks', 'genre_list', 'release_date', 'is_explicit', 'album_cover_url', 'uri']
        ## spotify_data.append(head)

        # Getting the data obtained from Spotify API into the list of lists
        for rank, uri in enumerate(uris):
            track = sp.track(uri)

            song = track['name']
            # artist_aux = [artist['name'] for artist in track['album']['artists']]
            artist_aux = [artist['name'] for artist in track['artists']]
            artist_ids = [artist['id'] for artist in track['artists']]  # mine
            genres = [sp.artist(artist_id)['genres'] for artist_id in artist_ids]
            genres = [genre for genre_lst in genres for genre in genre_lst]
            genres = np.unique(genres)
            if len(artist_aux) > 1:
                artist = artist_aux[0] + ' & ' + ' & '.join(artist_aux[1:])
            else:
                artist = artist_aux[0]
            popularity = track['popularity']
            duration_ms = track['duration_ms']
            album_type = track['album']['album_type']
            total_tracks = track['album']['total_tracks']
            release_date = track['album']['release_date']
            is_explicit = track['explicit']
            album_cover_url = track['album']['images'][0]['url']
            if len(genres) > 1:
                genre_list = genres[0] + ' & ' + ' & '.join(genres[1:])
            elif len(genres) == 1:
                genre_list = genres[0]
            else: # For debug purpose
                genre_list = None

            spotify_data.append([today, rank+1, song, artist, popularity, duration_ms, album_type, total_tracks, genre_list, release_date, is_explicit, album_cover_url, uri])

        ## Pass data into a csv file
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', encoding="utf-8", newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(head)

        with open(csv_file_path, 'a', encoding="utf-8", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for data_list in spotify_data:
                writer.writerow(data_list)