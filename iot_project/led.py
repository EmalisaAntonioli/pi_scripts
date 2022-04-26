import RPi.GPIO as GPIO
from datetime import datetime


def turn_on_light(pin):
    GPIO.setmode(GPIO.BCM) 

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

def turn_off_light(pin):
    GPIO.setmode(GPIO.BCM) 

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

def control_light(pin_light):
    # as fishes need 10 to 12 hours of light (https://www.tetra-fish.com/learning-center/get-educated/aquarium-lighting-basics.aspx#:~:text=Unlike%20plants%2C%20fish%20do%20not,a%20rating%20of%205500%20Kelvin.&text=How%20long%20should%20I%20keep,hours%20a%20day%20is%20sufficient) 
    # the light will automatically be on every day from 7 am to 6 pm
    if (datetime.now().hour >= 7 and datetime.now().hour <= 18):
        turn_on_light(pin_light)
    else:
        turn_off_light(pin_light)

