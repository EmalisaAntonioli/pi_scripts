import feed_motor
import water_level
import lcd

import RPi.GPIO as GPIO
import threading

# Measure the distance between the ultrasonic sensor and the water level
task1 = threading.Thread(target=water_level.control_pump, args=(26, 19, 1, 12))
# Let te motor for the feeding disc run
# Enter the pins to which the stepper motor is attached and the frequency of feeding
task2 = threading.Thread(target=feed_motor.step, args=(18, 23, 24, 25, 10))

task3 = threading.Thread(target=lcd.print_current_time)

task1.start()
task2.start()
task3.start()

try:
    pass
except KeyboardInterrupt:
    lcd.clear_display()
    print("hello")
    GPIO.cleanup()
