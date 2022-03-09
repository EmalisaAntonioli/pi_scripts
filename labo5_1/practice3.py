#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18

#blinking function
def blink(pin):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.3)
    GPIO.output(pin, 0)
    time.sleep(0.3)

# main program blink GPIO24 infinitely long
while(True):
    blink(17)
    blink(18)
    blink(23)
    blink(25)
