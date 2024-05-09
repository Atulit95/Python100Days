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
user_id=sp.current_user()["id"]
track="Hass Hass"+" "+"2024"
td=sp.search(q=track,type="track")["tracks"]["items"][0]["uri"]
sp.user_playlist_add_tracks(user=user_id,playlist_id=list_of_playlist[user_playlist_name],uris=uri,position=0)

# tl=sp.track("spotify:track:"+td)
print(td)
# list_of_playlist={}
# for i in range(0,len(td)):
#     list_of_playlist[f"{(td[i]["name"])}"]=f'{td[i]["id"]}'

Hello
