#blink LED 
import RPi.GPIO as GPIO
import time
# to use raspberry PI GPIO numbers
GPIO.setmode(GPIO.BCM) #GPIO18

#blinking function
def blink(pin, aantalBlinks, periode, dutyCycle):
    # setup GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    tijdhoog = periode * dutyCycle/100
    tijdlaag = periode - tijdhoog 
    for teller in range(0, aantalBlinks) :
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(tijdhoog)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(tijdlaag)

blink(18, 20, 0.5, 75)

GPIO.cleanup()
print("program executed")
