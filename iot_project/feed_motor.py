import lcd
import time
import RPi.GPIO as GPIO

def full_step(pin1, pin2):
    # Turn the motor
    GPIO.output(pin1, 1)
    GPIO.output(pin2, 1)
    time.sleep(0.01)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)
    time.sleep(0.01)

def turn_feeding_disc(pin1, pin2, pin3, pin4):
    # Turn the feeding disc to drop food
    # Change the denominator in the range depending on the amount of holes in the disc
    for i in range(int(490/24)):
            full_step(pin1, pin2)
            full_step(pin2, pin3)
            full_step(pin3, pin4)
            full_step(pin4, pin1)
    
    print('fishes have been fed')


def turn_feeding_disc_reverse(pin1, pin2, pin3, pin4):
    # Turn the feeding disc to drop food, but in reverse
    # Change the denominator in the range depending on the amount of holes in the disc
    for i in range(int(490/24)):
            full_step(pin1, pin4)
            full_step(pin4, pin3)
            full_step(pin3, pin2)
            full_step(pin2, pin1)

def timed_feeding(pin1, pin2, pin3, pin4, frequency):
    # Calculate delay between pplanned feedings
    delay = 1440 / frequency

    while(True):
        # Take a step big enough for the disc to let a pellet of food drop
        turn_feeding_disc(pin1, pin2, pin3, pin4)

        # Wait until the next feeding time
        for i in range(int(delay)):
            lcd.print_message("new feed in\n%i minutes" % (delay - i))
            time.sleep(60)
