#!/usr/bin/env python3

import os.path
import requests
import io
import time
from dotenv import load_dotenv
from src import apilookup
from src import display

load_dotenv()

image_lookup = apilookup.ApiLookup(os.getenv('HDMI_ENDPOINT'), os.getenv('HDMI_WIDTH'), os.getenv('HDMI_HEIGHT'))
image_display = display.Display(os.path.dirname(os.path.realpath(__file__))+'/fonts/', os.getenv('HDMI_WIDTH'), os.getenv('HDMI_HEIGHT'))

def display_image():
    try:
        next_image = image_lookup.get_random_image()
        response = requests.get(next_image["url"])
        response.raise_for_status()
        image_bytes = io.BytesIO(response.content)
        image_display.send_to_hdmi(next_image, image_bytes)
    except Exception as e:
        print(f"[ERROR] display_image failed: {e!r}")
    # Always sleep, even after error
    duration = int(os.getenv('HDMI_DURATION', '10'))
    time.sleep(duration)

try:
    while True:
        display_image()
except KeyboardInterrupt:
    print('Finished!')
