# Drive the stepper motor
# The stepper motor is attached to four, vairable pins
# Make sure the pins are in the right (i.e. neighbouring) order
import lcd

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

def full_step(pin1, pin2):
    # Setup GPIO output channel
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)

    # Turn the motor
    GPIO.output(pin1, 1)
    GPIO.output(pin2, 1)
    time.sleep(0.01)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)
    time.sleep(0.01)

def step(pin1, pin2, pin3, pin4, frequency):
    # It is assumed that frequenct is equal to the amount of slots in the feeding disc
    # Calculate delay
    delay = 1440 / frequency
    while(True):
        # Take a step big enough for the disc to let a pellet of food drop
        # Adjust the range to adjust how far the motor turns per feed
        for i in range(int(500/frequency)):
            full_step(pin1, pin2)
            full_step(pin2, pin3)
            full_step(pin3, pin4)
            full_step(pin4, pin1)
            print(i)
        print('fishes have been fed')
        # Wait until the next feeding time
        for i in range(int(delay)):
            lcd.print_message("new feed in\n%i minutes" % (delay - i))
            print("new feed in\n%i minutes" % (delay - i))
            time.sleep(10)
