# import requests
CLIENT_ID="5f82dfbdd6864b96ba27665af2635f4a"

# para={
#     "response_type": "code",
#     "redirect_uri":"http://localhost:3000",
#     "client_id":CLIENT_ID
# }

# header={
#     "Authorization": "Bearer 464a7de56ba548be9c1ae82283d8e539"
# }
# response=requests.get("https://api.spotify.com/v1/me",headers=header,params=para)
# print(response.raise_for_status())

CLIENT_SECRET="8ac71543bae6440f9aef3a4d559f9bf3"
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:3000",
                                               scope = "user-library-read"))
print(sp.current_user_playlists())