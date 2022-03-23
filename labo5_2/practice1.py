#blink LED 
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN)


#blinking function
def blink(pin):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

# main program blink GPIO18 infinitely long
while(True):
    if (GPIO.input(17) == 1):
        print("LED blinks")
        blink(18)
    else:
        print("LED does not blink")
        time.sleep(1)


