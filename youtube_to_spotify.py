import json
import requests
import os
import youtube_dl

from ytmusicapi import YTMusic
from private import spotify_user_id, spotify_token

class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}

    def get_youtube_client(self):
        ytmusic = YTMusic("headers_auth.json")

        return ytmusic

    def get_liked_videos(self):
        likedSongs = self.youtube_client.get_liked_songs(100000)
        
        for item in likedSongs["tracks"]:
            video_title = item["title"]

            youtube_url = "https://www.youtube.com/watch?v={}".format(item["videoId"])

            video = youtube_dl.YoutubeDL({}).extract_info(youtube_url, download=False)

            song_name = video["track"]
            artist = video["artist"]
            
            if song_name is not None and artist is not None:
                spotify_uri = self.get_spotify_uri(song_name, artist)
                if spotify_uri is not None:
                    self.all_song_info[video_title]={
                        "song_name": song_name,
                        "artist": artist,

                        "spotify_uri": spotify_uri
                }

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Your YouTube Liked Music",
            "description": "Compilation of all your liked YouTube videos",
            "public": False
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data = request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        return response_json["id"]

    def get_spotify_uri(self, track, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offest=0&limit=20".format(
            track,
            artist
        )

        response =  requests.get(
            query,
            headers={
                "Content-Type" : "application/json",
                "Authorization" : "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        
        if songs:
            uri = songs[0]["uri"]
        else:
            uri = None
        return uri
    
    def add_song_to_playlist(self):
        self.get_liked_videos()
        

        uris = [info["spotify_uri"]
                for song, info in self.all_song_info.items()]
        
        n = 50
        splituris = [uris[i * n:(i + 1) * n] for i in range((len(uris) + n - 1) // n )]

            
        playlist_id = self.create_playlist()

        for suburis in splituris:
            request_data = json.dumps(suburis)

            query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

            response = requests.post(
                query,
                data = request_data,
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(spotify_token)
                }
            )
        
        response_json = response.json()
        return response_json

if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()

