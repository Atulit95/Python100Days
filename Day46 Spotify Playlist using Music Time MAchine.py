import datetime as dt
import requests
from bs4 import BeautifulSoup

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
print(list)
