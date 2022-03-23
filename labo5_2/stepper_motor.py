#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18
# GPIO.setup(18, GPIO.OUT)

def wave_step(pin):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.01)
    GPIO.output(pin, 0)
    time.sleep(0.01)

def full_step(pin1, pin2):
    # setup GPIO output channel
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)

    GPIO.output(pin1, 1)
    GPIO.output(pin2, 1)

    time.sleep(0.01)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)

    time.sleep(0.01)

# waver drive
# while(True):
#     wave_step(18)
#     wave_step(23)
#     wave_step(25)
#     wave_step(21)

# full step
while(True):
    full_step(18, 23)
    full_step(23, 25)
    full_step(25, 21)
    full_step(21, 18)
