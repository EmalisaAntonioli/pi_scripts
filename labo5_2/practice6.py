#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18
GPIO.setup(17, GPIO.IN)
GPIO.setup(23, GPIO.IN)


def switch(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    time.sleep(0.5)
    GPIO.output(pin, 1)
    time.sleep(0.5)

while(True):
    if (GPIO.input(17) == 0):
        print("switch 18")
        switch(18)
    elif (GPIO.input(23) == 0):
        print("switch 22")
        switch(22)
    else:
        print("no switch")
        time.sleep(0.5)