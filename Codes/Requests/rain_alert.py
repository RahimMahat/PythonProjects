#!/usr/bin/env python3
import requests
from twilio.rest import Client

# you'll get ac_sid and auth_token once you sign up for twilio
twilio_account_sid = ""
twilio_auth_token = ""

# you'll get the api key once you sign up for openweather
openwheather_link = "openweathermap.org"
my_api_key = ""
owm_api = "https://api.openweathermap.org/data/2.5/onecall"

# TODO: Getting weather data from openweather
# when you test the api_key you'll easily get latitude and longitude
# Kanpur was raining at the time so to check it. It's their lat,lng
weather_params = {
    "lat": 26.449923,
    "lon": 80.331871,
    "appid": my_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(owm_api, params=weather_params)
# response.raise_for_status()
weather_data = response.json()

# id = weather_data["hourly"][0]["weather"][0]["id"]
# getting 12 hours of hourly data list
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # from id= 2xx to 7xx the weather is under certain atmospheric condition
    if int(condition_code) < 700:
        will_rain = True

# TODO: Setting up our twilio client
# if the condition code gives us rainy code
if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
            # message body for the sms
            body="It's going to 🌧 today, so bring an ☔",
            # phone number given by the twilio
            from_="",
            # your verified number
            to=""
        )
    print(message.status)
