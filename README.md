# YouTube-To-Spotify
A python script that takes your liked music videos from YouTube and converts them into a Spotify playlist. Utilizes ytmusicapi by sigma67 and Spotify web API

## Getting credentials to access your YouTube Music account
### Step 1
Visit https://ytmusicapi.readthedocs.io/en/latest/setup.html and follow the given steps this should help you copy the required headers
### Step 2
Open `setupytmusicapi.py` and paste the information you copied there <br>
Run the program and it will generate `headers_auth.json` <br>
After that, you are done! Your credentials should not expire anytime soon

## Getting credentials to access your Spotify account
### Step 1
Visit https://developer.spotify.com/console/post-playlists/ <br> 
From this website, we can obtain the OAuth token for Spotify <br>
You can get the token by clicking the "Get Token" button near the bottom of the page and making sure to include the required scopes for this endpoint <br>
This OAuth token expires very frequently so using this website is great resource to get new tokens and making sure that your old tokens are still working.
### Step 2
Copy this OAuth token as well as your Spotify user id (Spotify username) and place them in the `private.py` file.
