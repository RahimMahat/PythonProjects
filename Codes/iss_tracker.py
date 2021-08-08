#!/usr/bin/env python3

import requests
import smtplib
import time
import datetime as dt
# CONSTANTS
MY_LAT = "you can get you longitude and latitude"
MY_LNG = "from latlong.net"
MY_EMAIL = "youremail@gmail.com"
MY_PASWD = "your@password"

link_for_iss_notify = "http://open-notify.org/Open-Notify-API/ISS-Location-Now/"
api_url = "http://api.open-notify.org/iss-now.json"


# TODO: Check the iss is near to your location
def is_iss_overhead() -> bool:
    response = requests.get(url=api_url)
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True


# TODO: Check if it's the night time so we can spot the iss
def is_dark() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    # getting sunset and sunrise time from an api
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = dt.datetime.now().hour

    if hour_now >= sunset_hour or hour_now <= sunrise_hour:
        return True


while True:
    # the script will run after every 15 minutes
    time.sleep(60*15)
    # if both the functions return true then send me a mail
    if is_iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASWD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:International Space Station\n\nThe ISS is above you in the sky"
            )
