import feed_motor
import water_level
import lcd
import buttons
import led

import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM) 

led.startup_light(5) 

# Measure the distance between the ultrasonic sensor and the water level
task1 = threading.Thread(target=water_level.control_pump, args=(26, 19, 1, 12, 17))
# Let te motor for the feeding disc run
# Enter the pins to which the stepper motor is attached and the frequency of feeding
task2 = threading.Thread(target=feed_motor.step, args=(18, 23, 24, 25, 10))
# Display the current time on the screen
task3 = threading.Thread(target=lcd.print_current_time)
# Keep an eye on the buttons
task4 = threading.Thread(target=buttons.check_buttons, args=(17, 12))
# Control the lights with time
task5 = threading.Thread(target=led.control_light, args=([5]))
task6 = threading.Thread(target=buttons.motor_button, args=(21, 18, 23, 24, 25))
task7 = threading.Thread(target=buttons.light_button, args=(5, 13))

task1.start()
task2.start()
task3.start()
task4.start()
task5.start()
task6.start()
task7.start()

# while(True):
#     try:
#         pass
#     except KeyboardInterrupt:
#         lcd.clear_display()
#         print("hello")
#         # GPIO.cleanup()
