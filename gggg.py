from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'

def is_stream_online(username):

    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as ffffffffasasd:
    ffffffffasasd.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    ffffffffasasd.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #"#live-channel-stream-information"
    url = "https://www.twitch.tv/brutalles"
    ffffffffasasd.uc_open_with_reconnect(url, 4)
    ffffffffasasd.sleep(14)
    ffffffffasasd.uc_gui_click_captcha()
    ffffffffasasd.sleep(1)
    ffffffffasasd.uc_gui_handle_captcha()
    ffffffffasasd.sleep(4)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        ffffffffasasd.uc_open_with_reconnect(url, 5)
        if ffffffffasasd.is_element_present('button:contains("Accept")'):
            ffffffffasasd.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            ffffffffasasd2 = ffffffffasasd.get_new_driver(undetectable=True)
            ffffffffasasd2.uc_open_with_reconnect(url, 5)
            ffffffffasasd.sleep(10)
            if ffffffffasasd2.is_element_present('button:contains("Accept")'):
                ffffffffasasd2.uc_click('button:contains("Accept")', reconnect_time=4)
            while ffffffffasasd.is_element_present("#live-channel-stream-information"):
                ffffffffasasd.sleep(150)
            ffffffffasasd.quit_extra_driver()
    ffffffffasasd.sleep(1)
