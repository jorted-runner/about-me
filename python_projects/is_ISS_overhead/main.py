import time

import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

MY_LAT = float(os.environ.get("MY_LAT"))
MY_LONG = float(os.environ.get("MY_LONG"))
my_email = os.environ.get("my_email")
my_pass = os.environ.get("my_pass")

msg_dark = "Subject: ISS Satellite\n\nHurry outside! The Iss Satellite is passing overhead and is visible!"
msg_light = "Subject: ISS Satellite\n\nThe ISS Satellite is passing overhead. " \
            "You won't be able to see it because its still day time but its fun to know."


def can_i_see_iss():
    if MY_LONG - 5 < iss_longitude < MY_LONG + 5 and MY_LAT - 5 < iss_latitude < MY_LAT + 5:
        return True
    else:
        return False


def is_it_dark(my_utc_time, utc_sunrise, utc_sunset):
    if utc_sunset < my_utc_time < utc_sunrise:
        return True
    else:
        return False


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.environ.get("to_addrs"),
            msg=message
        )


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


running = True
while running:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    utc_time_now = datetime.now().utcnow()
    hour = utc_time_now.hour

    can_see = can_i_see_iss()
    dark = is_it_dark(hour, sunrise, sunset)
    if can_see and dark:
        send_email(msg_dark)
    elif can_see:
        send_email(msg_light)
    time.sleep(60)

