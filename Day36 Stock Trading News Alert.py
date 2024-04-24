import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

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
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": "",
}
tesla_stock_response = requests.get(
    url="https://www.alphavantage.co/query", params=tesla_stock_parameters
)
tesla_stock_response.raise_for_status()
stock_data = tesla_stock_response.json()

yesterday_closing_data = float(
    stock_data["Time Series (Daily)"][f"{year}-{month}-{day-1}"]["4. close"]
)

day_before_yesterday_closing_data = float(
    stock_data["Time Series (Daily)"][f"{year}-{month}-{day-2}"]["4. close"]
)

difference_in_closing_values = yesterday_closing_data-day_before_yesterday_closing_data

if difference_in_closing_values<0:
    percent_decrease=

print(difference_in_closing_values)

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
