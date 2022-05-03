import water_level
import feed_motor
import led

from ctypes.wintypes import PLARGE_INTEGER
import RPi.GPIO as GPIO
import time
from datetime import datetime

def motor_button(pin_motor, motor1, motor2, motor3, motor4):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_motor, GPIO.IN)

    while(True):
        if (GPIO.input(pin_motor) == 0):
            button_switched = datetime.now()

            while(GPIO.input(pin_motor) == 0):
                pass

            button_released = datetime.now()
            if (button_released - button_switched).total_seconds() > 0.5:
                print("switch motor reverse")
                feed_motor.turn_feeding_disc_reverse(motor1, motor2, motor3, motor4)
            else:
                print("switch motor")
                feed_motor.turn_feeding_disc(motor1, motor2, motor3, motor4)
        
        time.sleep(0.1)
        
def light_button(pin_light, pin_light_button):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_light_button, GPIO.IN)
    
    while(True):
        if (GPIO.input(pin_light_button) == 0):
            if GPIO.input(pin_light):
                led.turn_on_light(pin_light)
                # anti-bouncing
                time.sleep(0.1)
            else:
                led.turn_off_light(pin_light)
                # anti-bouncing
                time.sleep(0.1)
        time.sleep(0.1)      


def check_buttons(pin_pump_button, pin_pump):
    # While the button is pressed in, the pump will be on
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin_pump_button, GPIO.IN)

    while(True):
        # PUMP
        if (GPIO.input(pin_pump_button) == 0):

            water_level.switch_pump("on", pin_pump)
            while(GPIO.input(pin_pump_button) == 0):
                time.sleep(0.01)
            water_level.switch_pump("off",pin_pump)

        time.sleep(0.2)
