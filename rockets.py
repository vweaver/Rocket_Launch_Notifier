import os
import requests
from twilio.rest import Client
from datetime import datetime
from dateutil import tz
from config import Config


account_sid = Config.account_sid
auth_token = Config.auth_token
cells = Config.cells
twilio_number = Config.twilio_number


def send_sms(cell, msg):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_=twilio_number, to=cell)
    print(message.status)


def get_launches():
    RLL_url = "https://fdo.rocketlaunch.live/json/launches/next/5"
    response = requests.get(url=RLL_url)
    response.raise_for_status()
    return response.json()["result"]


def utc_to_est(utc_string):
    """returns a 12h formatted local time from a UTC data time string"""
    from_zone = tz.gettz("UTC")
    to_zone = tz.gettz("America/New_York")
    utc = datetime.strptime(utc_string, "%Y-%m-%dT%H:%MZ")
    utc = utc.replace(tzinfo=from_zone)
    est = utc.astimezone(to_zone)
    est_12h = est.strftime("%I:%M %p")
    return est_12h


if __name__ == "__main__":
    launch_data = get_launches()
    va_lauches = [
        l for _, l in enumerate(launch_data) if l["pad"]["location"]["id"] == 88
    ]

    msgs = []
    for l in va_lauches:
        est = utc_to_est(l["win_open"])
        msgs.append(f"{l['launch_description']} {est} (EST)")

    for msg in msgs:
        for cell in cells:
            send_sms(cell, msg)
