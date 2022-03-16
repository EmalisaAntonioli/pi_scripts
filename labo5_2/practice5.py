#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18
GPIO.setup(17, GPIO.IN)


#blinking function
def blink(pin):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

# main program sends SOS on GPIO 18
while(True):
    if (GPIO.input(17) == 0):
        blink(18)
        blink(23)
        blink(25)
        blink(21)
        # time.sleep(1)
        
    else: 
        blink(21)
        blink(25)
        blink(23)
        blink(18)
        # time.sleep(1)


