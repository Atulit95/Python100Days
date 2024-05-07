import requests
from bs4 import BeautifulSoup

response=requests.get(f"https://www.billboard.com/charts/hot-100/{"2024-04-24"}/")

billboard_website=response.text

soup=BeautifulSoup(billboard_website,"html.parser")

list=[title.getText().strip() for title in soup.select("li ul li h3")]
print(list)                                                       