import RPi.GPIO as GPIO
import time
from datetime import datetime
import lcd

def depth_measurement(pin_in, pin_out):
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
    GPIO.setup(pin, GPIO.OUT)
    if status == "on":
        GPIO.output(pin, 0)
    if status == "off":
        GPIO.output(pin, 1)

def control_pump(pin_in, pin_out, max_distance, pin_pump, pin_button):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_in, GPIO.IN)
    GPIO.setup(pin_button, GPIO.IN)

    GPIO.setup(pin_out, GPIO.OUT)

    while(True):
        distance = depth_measurement(pin_in, pin_out)
        print("water distance: %.4f" % distance)
        lcd.print_message("waterlevel:\n %.3f m" % distance)

        if distance > max_distance == 0:
            # If the water level is too low, turn the pump on
            switch_pump("on", pin_pump)
            print("The pump has been turned on")

            while(distance > max_distance):
                distance = depth_measurement(pin_in, pin_out)
                print("water distance: %.4f" % distance)
                lcd.print_message("%.3f m" % distance)
                time.sleep(2)

            

            # Once the water level is no longer too low, turn the pump off
            switch_pump("off", pin_pump)
            print("The pump has been turned off")
                
        time.sleep(4)