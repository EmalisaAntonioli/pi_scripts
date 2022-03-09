#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18

#blinking function
def blink(pin1, pin2):
    # setup GPIO output channel
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.output(pin1, 1)
    GPIO.output(pin2, 1)
    time.sleep(1)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)
    time.sleep(1)

# main program blink GPIO24 infinitely long
while(True):
    blink(17, 23)
    blink(18, 25)
