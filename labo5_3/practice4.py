
import RPi.GPIO as GPIO
import time
import datetime
GPIO.cleanup()

GPIO.setmode(GPIO.BCM) 

while (True):
    # set the GPIO as output and drive it Low
    # this ensures that no charge is present in capacitor
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18,0)
    time.sleep(0.1)
    # now set the GPIO as input
    # this will start a flow of current through the resistors and through the capacitor to ground
    # the voltage through the capacitor starts to rise
    GPIO.setup(18, GPIO.IN)

    starttime = datetime.datetime.now() 
    while (GPIO.input(18) == 0):
        pass
    endtime = datetime.datetime.now() 

    print((endtime - starttime).microseconds)

    time.sleep(0.5)
