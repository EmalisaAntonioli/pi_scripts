import RPi.GPIO as GPIO
import time
import datetime
GPIO.cleanup()

GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

while(True):
    GPIO.output(17, 1)
    time.sleep(0.00001)
    GPIO.output(17, 0)

    while(GPIO.input(18) == 0):
        pass

    signaalhigh = datetime.datetime.now()

    while(GPIO.input(18) == 1):
        pass

    signaallow = datetime.datetime.now()
    timepassed = signaallow - signaalhigh
    distance = timepassed.total_seconds() * 170
    print(distance)

    time.sleep(0.5)
