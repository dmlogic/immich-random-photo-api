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
    next_image = image_lookup.get_random_image()
    try:
        response = requests.get(next_image["url"])
        image_bytes = io.BytesIO(response.content)
        image_display.send_to_hdmi(next_image, image_bytes)
        time.sleep(int(os.getenv('HDMI_DURATION')))
    except Exception as e:
        # print(f"An error occurred: {e}")
        time.sleep(int(os.getenv('HDMI_DURATION')))
        display_image()

try:
    while True:
        display_image()
except KeyboardInterrupt:
    print('Finished!')
