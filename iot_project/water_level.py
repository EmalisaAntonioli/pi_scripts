import RPi.GPIO as GPIO
import time
from datetime import datetime
import lcd
import ubeac

def depth_measurement(pin_in, pin_out):
    GPIO.setmode(GPIO.BCM) 
    GPIO.output(pin_out, 1)
    time.sleep(0.00001)
    GPIO.output(pin_out, 0)

    while(GPIO.input(pin_in) == 0):
        pass

    signalhigh = datetime.now()

    while(GPIO.input(pin_in) == 1):
        pass

    signallow = datetime.now()

    timepassed = signallow - signalhigh
    distance = timepassed.total_seconds() * 170
    return distance

def switch_pump(status, pin):
    if status == "on":
        GPIO.output(pin, 0)
    if status == "off":
        GPIO.output(pin, 1)

def control_pump(pin_in, pin_out, max_distance, pin_pump):
    while(True):
        distance = depth_measurement(pin_in, pin_out)
        lcd.print_message("waterlevel:\n%.3f m" % distance)

        if distance > max_distance:
            # If the water level is too low, turn the pump on
            switch_pump("on", pin_pump)
            print("The pump has been turned on")

            while(distance > max_distance):
                time.sleep(1)
                distance = depth_measurement(pin_in, pin_out)
                lcd.print_message("waterlevel:\n%.3f m" % distance)

            # Once the water level is no longer too low, turn the pump off
            switch_pump("off", pin_pump)
            print("The pump has been turned off")
                
        time.sleep(7)