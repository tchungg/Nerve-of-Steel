"""
This program is used for MGTC28, In class exercise 4.
nerve_of_steel uses the time library to help keep track of time and the random library to pick a random time

Pseudocode:
Display Players stand
Sleep for a random time between 5 to 25
Once timer is up, present a winner

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



