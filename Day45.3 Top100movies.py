import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

titles = [
    title.getText().split(") ")[-1]
    for title in soup.find_all(name="h3", class_="title")
]
inverted_list = titles[::-1]

inverted_list[11] = inverted_list[11].split(": ")[1]
inverted_list[58] = inverted_list[58].split("â\x80\x93 ")[1]
# print(inverted_list[58])

with open("100MustWatchMovies.txt","w") as file:
    for title_in_list in inverted_list:
        file.write(f"{title_in_list}\n")
