!pip install requests

url = 'https://accounts.spotify.com/api/token'
headers = {}
data = {}

import base64
from secrets import *  # This "secret.py" file contains my clientID and client secret

message = f"{clientID}:{clientSecret}"

messageBytes = message.encode('ascii')

base64Bytes = base64.b64encode(messageBytes)

base64Message = base64Bytes.decode('ascii')

token_data={
    'grant_type': 'client_credentials'
}
token_headers = {
    'Authorization': f'Basic {base64Message}' #Basic <base64 encoded client_id:client_secret>
}
token_headers

import requests
import json

r = requests.post(url, data=token_data, headers=token_headers)
print(r.json())

token = r.json()['access_token']

# First, you need to have your playlist in Spotify. 
# Right click on your playlist and then "Copy playlist link". 
# You will see the playlist ID at the end of https://open.spotify.com/playlist/
playlistId = "Plug your playlist ID here" 
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
headers = {
    "Authorization": "Bearer " + token
}
res = requests.get(url=playlistUrl, headers=headers)
print(res)

# You might see an error indicating that your token expred. 
# In this case, just go back to the step getting a token and run the steps again. This is actually a bit cumbersome ... 
print(json.dumps(res.json(), indent=2))

# Then yyou will see Json data including like the items below. 
     "name": "Brighter Days",
            "release_date": "2018-09-28",
            "release_date_precision": "day",
            "total_tracks": 16,
            "type": "album",
            "uri": "spotify:album:5rr0xAQfk01cPi1N37jX11"