#!/Users/kellyeldritch/.local/youtube/music/.venv/bin/python

import os
import subprocess
import sys
from ytmusicapi import YTMusic

def authenticate_ytmusic():
    if not os.path.exists('oauth.json'):
        print("Authentication file 'oauth.json' is missing. Launching authentication process...")
        subprocess.run(['ytmusicapi', 'oauth'])
    
    try:
        return YTMusic('oauth.json')
    except Exception as e:
        print("An error occurred during YTMusic initialization:", e)
        return None

def get_input_parameters():
    if len(sys.argv) == 3:
        playlist_id = sys.argv[1]
        file_path = sys.argv[2]
        with open(file_path, 'r') as file:
            video_ids = file.read().split(',')
    else:
        playlist_id = input("Enter the playlist ID: ")
        video_ids = input("Enter the comma-separated list of video IDs: ").split(',')
    return playlist_id, video_ids

# Main code
yt = authenticate_ytmusic()  # Attempt to authenticate

if yt:
    playlist_id, song_ids = get_input_parameters()
    # Clean up any whitespace in the song IDs
    song_ids = [song_id.strip() for song_id in song_ids]
    
    # Try adding songs to the playlist
    for song_id in song_ids:
        try:
            yt.add_playlist_items(playlist_id, [song_id.strip()])
            print("Song added to the playlist successfully.")
        except Exception as e:
            print("An error occurred when adding songs to the playlist:", e)
else:
    print("Authentication failed. Please rerun the script after completing the authentication process.")
