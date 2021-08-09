#!/usr/bin/env python3
import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
alpha_vantage_api_key = "xxxxxxxxxxxxxxxxxxxxx"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "xxxxxxxxxxxxxxxxx"

TWILIO_AC_SID = "xxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxx"

# TODO:1. Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "1min",
    "apikey": alpha_vantage_api_key

}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# making list comprehension to only get required metadata from the above json response
data_list = [value for (key, value) in data.items()]
# variable names speak for themselves
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

# TODO:2. Get the day before yesterday's closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# TODO:3. Find the positive difference between 1 and 2.
# as the values from json data is string so typecasting
difference = round(float(yesterday_closing_price) -
                   float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

# TODO:4, Work out the percentage difference in price between closing price of 1 and 2.
diff_percent = (difference / float(yesterday_closing_price)) * 100
# print(diff_percent)

# TODO:5. If todo4 percentage is greater than 5 than "Get News"
# abs will return positive difference
if abs(diff_percent) > 5:
    new_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]
    # we only want max three news articles
    three_articles = articles[:3]
    # print(three_articles)

# TODO:6. Use twilio to send a separate message with each article's title and description to your phone number

# creating a new list comprehension for the 3 articles headlines and descriptions
formatted_articles = [
    f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# send each article as a separate message via twilio
client = Client(TWILIO_AC_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        # phone number from twilio
        from_="xxxxxxxxxx",
        # verified phone number to send msg
        to="xxxxxxxxxx"
    )
    print(message.status)
