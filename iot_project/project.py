from re import L
import feed_motor
import water_level
import lcd
import buttons
import led
import ubeac
from pi_audio_classify.classify import classify;

import threading
import RPi.GPIO as GPIO


# Initiate all GPIO pins
button_pump = 17
button_light = 13
button_light_timer = 22
button_motor = 21
motor_1 = 18
motor_2 = 23
motor_3 = 24
motor_4 = 25
pump = 12
sonic_sensor_trg = 19
sonic_sensor_echo = 26
light = 5

input_pins = [button_pump, button_light, button_light_timer, button_motor, sonic_sensor_echo]
output_pins = [motor_1, motor_2, motor_3, motor_4, pump, sonic_sensor_trg, light]

GPIO.setmode(GPIO.BCM) 
for pin in input_pins:
    GPIO.setup(pin, GPIO.IN)

for pin in output_pins:
    GPIO.setup(pin, GPIO.OUT)

# Start the programme
led.startup_light(light) 

task1 = threading.Thread(target=water_level.control_pump, args=(sonic_sensor_echo, sonic_sensor_trg, 0.05, pump))
task2 = threading.Thread(target=feed_motor.timed_feeding, args=(motor_1, motor_2, motor_3, motor_4, 10))
task3 = threading.Thread(target=lcd.print_current_time)
task4 = threading.Thread(target=buttons.pump_button, args=(button_pump, pump))
task5 = threading.Thread(target=led.control_light, args=([light]))
task6 = threading.Thread(target=buttons.motor_button, args=(button_motor, motor_1, motor_2, motor_3, motor_4))
task7 = threading.Thread(target=buttons.light_button, args=(light, button_light))
task8 = threading.Thread(target=ubeac.ubeac, args=(sonic_sensor_echo, sonic_sensor_trg, light, pump))
task9 = threading.Thread(target=buttons.light_timer, args=(light, button_light_timer))
task10 = threading.Thread(target=classify, args=(motor_1, motor_2, motor_3, motor_4))

task1.start()
task2.start()
task3.start()
task4.start()
task5.start()
task6.start()
task7.start()
# task8.start()
task9.start()
task10.start()
