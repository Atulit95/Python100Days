import requests
import datetime as dt
import math
from twilio.rest import Client
import random

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "ACbc0ff2189cba7187b398f222a41e4bf0"
auth_token = "2c7418e9f93599422f880b43599ecae8"


def percent_incr_or_decr(previous_day_data, day_before_previous_day_data):
    difference_in_closing_values = previous_day_data - day_before_previous_day_data

    if difference_in_closing_values < 0:
        percent_incr_or_decr = (
            (-1 * difference_in_closing_values) / day_before_previous_day_data
        ) * 100
    elif difference_in_closing_values > 0:
        percent_incr_or_decr = (difference_in_closing_values / previous_day_data) * 100
    else:
        percent_incr_or_decr = 0

    return math.ceil(percent_incr_or_decr)


def get_news(data):
    headline = []
    content = []
    url = []
    for i in range(0, 3):
        content.append(data["articles"][i]["description"])
        headline.append(data["articles"][i]["title"])
        url.append(data["articles"][i]["url"])

    return [headline, content, url]


time = dt.datetime.now()
day = time.day
if day < 10:
    day = "0" + str(day)
month = time.month
if month < 10:
    month = "0" + str(month)

year = time.year
# print(f"{day}--{month}--{year}")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

tesla_stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": "YIR4JGPZ7LXSA67E",
}
news_api_parameters = {
    "q": "tesla",
    "sortBy": "publishedAt",
    "apiKey": "581ed055fac4465ba2023cdeadb1e60f",
    "language": "en",
}

tesla_stock_response = requests.get(
    url="https://www.alphavantage.co/query", params=tesla_stock_parameters
)
news_reponse = requests.get(
    url="https://newsapi.org/v2/everything", params=news_api_parameters
)

tesla_stock_response.raise_for_status()
news_data = news_reponse.json()
news_list = get_news(news_data)


stock_data = tesla_stock_response.json()

yesterday_closing_data = float(
    stock_data["Time Series (Daily)"][f"{year}-{month}-{day-1}"]["4. close"]
)

day_before_yesterday_closing_data = float(
    stock_data["Time Series (Daily)"][f"{year}-{month}-{day-2}"]["4. close"]
)

percentage_value = percent_incr_or_decr(
    yesterday_closing_data, day_before_yesterday_closing_data
)
choice = random.randint(0, 2)
if (yesterday_closing_data - day_before_yesterday_closing_data) > 0:
    body_text = f"TSLA: 🔺{percentage_value}%\nHeadline:{news_list[0][choice]}.\nBrief: {news_list[1][choice]}\nUrl:{news_list[2][choice]}"
else:
    body_text = f"TSLA: 🔻{percentage_value}%\nHeadline:{news_list[0][choice]}.\nBrief: {news_list[1][choice]}\nUrl:{news_list[2][choice]}"

if percentage_value > 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body_text, from_="+12562039313", to="your_verified_no"
    )


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
