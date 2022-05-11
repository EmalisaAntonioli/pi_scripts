import water_level
import feed_motor
import led

from ctypes.wintypes import PLARGE_INTEGER
from datetime import datetime
import RPi.GPIO as GPIO
import time

def motor_button(pin_motor, motor1, motor2, motor3, motor4):
    # Watch the button that can release an extra feed
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_motor, GPIO.IN)

    while(True):
        if (GPIO.input(pin_motor) == 0):
            # Measure how long the button was pressed
            button_switched = datetime.now()
            while(GPIO.input(pin_motor) == 0):
                pass
            button_released = datetime.now()

            # When the button was pressed long the disc is turned in reverse
            if (button_released - button_switched).total_seconds() > 0.5:
                print("switch motor reverse")
                feed_motor.turn_feeding_disc_reverse(motor1, motor2, motor3, motor4)
            # A short press turns the disc forward
            else:
                print("switch motor")
                feed_motor.turn_feeding_disc(motor1, motor2, motor3, motor4)
        
        # Anti-bouncing
        time.sleep(0.2)
        
def light_button(pin_light, pin_light_button):
    # Watch the button that can turn the light on and off
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_light_button, GPIO.IN)
    
    while(True):
        if (GPIO.input(pin_light_button) == 0):
            # Turn the light on when off and vice versa
            if GPIO.input(pin_light):
                led.turn_on_light(pin_light)
                # Anti-bouncing
                time.sleep(0.2)
            else:
                led.turn_off_light(pin_light)
                # Anti-bouncing
                time.sleep(0.2)

def light_timer(pin_light, pin_light_button):
    # Watch the button that can turn the light on for 15 minutes
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_light_button, GPIO.IN)

    while(True):
        if (GPIO.input(pin_light_button) == 0):
            led.turn_on_light(pin_light)
            time.sleep(9)
            led.turn_off_light(pin_light)
        
        # Anti-bouncing
        time.sleep(0.2)

def pump_button(pin_pump_button, pin_pump):
    # Watch the button with which the pump can be turned on
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_pump_button, GPIO.IN)

    while(True):
        if (GPIO.input(pin_pump_button) == 0):
            # While the button is pressed, the pump will be on
            water_level.switch_pump("on", pin_pump)
            while(GPIO.input(pin_pump_button) == 0):
                time.sleep(0.01)
            water_level.switch_pump("off",pin_pump)

        #Anti-bouncing
        time.sleep(0.2)
