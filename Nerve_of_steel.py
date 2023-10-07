"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

import random

im = Image.open("times-up.jpeg")

print('Players stand')
sleep_time = random.randint(5,25)
print(f"Sleeping for {sleep_time} seconds. Players can sit down")


time.sleep(sleep_time)

print("Time's Up. Last to sit down wins!")

# how we know who sits down last 
last_to_sit_input = str (input("Enter who the last one to sit down was  "))
print (last_to_sit_input, "is the Winner!")



