# YouTube-To-Spotify
A python script that takes your liked music videos from YouTube and converts them into a Spotify playlist

## Getting credentials to access your YouTube account
### Step 1
Visit https://console.developers.google.com/apis/ From this website, you need to go to the API library and add the YouTube Data API v3.
### Step 2
Then you need to go to the OAuth consent screen and fill out the form. Once the form is filled out, you need to click "Add Users" and add your google email address as a user.
### Step 3
After this, you need to go to your Credentials tab and click on "Create Credentials".
This program requires OAuth Client ID and this is a desktop app so select those options. Click create and you are done with that!
### Step 4
You should now see your desktop in the OAuth 2.0 Client IDs tab. Click on the download icon on the far right and place the json file into the directory.
### Step 5
In the file `create_playlist.py`, you need to replace this line `client_secrets_file = "client_secret.json"` with whatever you named the json file you downloaded. The program should now have access to your YouTube credentials.

## Getting credentials to access your Spotify account
### Step 1
Visit https://developer.spotify.com/console/post-playlists/ From this website, we can obtain the OAuth token for Spotify. 
You can get the token by clicking the "Get Token" button near the bottom of the page and making sure to include the required scopes for this endpoint. 
This OAuth token expires very frequently so using this website is great resource to get new tokens and making sure that your old tokens are still working.
### Step 2
Copy this OAuth token as well as your Spotify user id (Spotify username) and place them in the `private.py` file.

## Running the program
Each time you run the program you will need to authorize Google to access your YouTube account. Simply click on the link, follow the instructions, and paste the authorization code the script should run.
