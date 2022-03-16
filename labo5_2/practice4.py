#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18
GPIO.setup(17, GPIO.IN)


#blinking function
def blink_short(pin):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

def blink_long(pin):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(1.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

def short_pulse(pin) :
    for i in range(3):
        blink_short(pin)

def long_pulse(pin):
    for i in range(3):
        blink_long(pin)

# main program sends SOS on GPIO 18
while(True):
    if (GPIO.input(17) == 0):
        short_pulse(18)
        long_pulse(18)
        short_pulse(18)
        print("hi")
        time.sleep(1)
        
    else: 
        print("2")
        time.sleep(1)


