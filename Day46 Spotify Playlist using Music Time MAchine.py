import datetime as dt
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_SECRET="8ac71543bae6440f9aef3a4d559f9bf3"
CLIENT_ID="5f82dfbdd6864b96ba27665af2635f4a"

curr_date = dt.datetime.now().date()

#--------------------------Date Checher-------------------------#
def valid_date_checker(date):
    split_date = date.split("-")
    if (
        int(split_date[0]) < curr_date.year
        and 0 < int(split_date[2]) <= 31
        and 0 < int(split_date[1]) <= 12
    ):
        return date
    elif (
        int(split_date[0]) == curr_date.year
        and int(split_date[1]) <= curr_date.month
        and int(split_date[2]) <= curr_date.day
    ):
        return date
    else:
        print(end="\033c")
        print("Invalid date!! Enter Valid date")
        valid_date_checker(
            input(
                "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
            )
        )

def dic_of_playlist_details():
    td=sp.current_user_playlists()["items"]
    list_of_playlist={}
    for i in range(0,len(td)):
        list_of_playlist[f"{(td[i]["name"])}"]=f'{td[i]["id"]}'

    return list_of_playlist

date = valid_date_checker(
    input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
    )
)

# Fetching Tpo 100 Songs of input date

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")

list = [title.getText().strip() for title in soup.select("li ul li h3")]


# ---------------------------------------------------------------------


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:3000",
                                               scope = "playlist-modify-public"))

user_playlist_name=input("Enter palylist name you desire:\n")

user_id=sp.current_user()["id"]

list_of_playlist=dic_of_playlist_details()
songs_uri=[]
if(user_playlist_name in list_of_playlist):
    for track in list:
        td=(sp.search(q=f"{track} {date[0:4]}",type="track")["tracks"]["items"][0]["album"]["id"])
        songs_uri.append(sp._get_uri(type=track,id=td))
        
# sp.user_playlist_add_tracks(user=user_id,playlist_id=list_of_playlist[user_playlist_name],tracks=songs_uri,position=None)
        
# else:
#     sp.user_playlist_create(user=user_id,name="Moosic",public=True)
#     sp.user_playlist_add_tracks(user=user_id,playlist_id="Moosic",tracks=list)

print(songs_uri)