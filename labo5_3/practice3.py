
import RPi.GPIO as GPIO
import time
GPIO.cleanup()

GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(25, GPIO.OUT)
# GPIO.setup(12, GPIO.OUT)


while(True):
    if (GPIO.input(17) == 0 or GPIO.input(12) == 0):
        print('lights on')
        GPIO.output(18, 1)
        time.sleep(0.5)
    else:
        print('lights off')
        GPIO.output(18, 0)
        time.sleep(0.5)