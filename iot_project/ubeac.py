import requests
import RPi.GPIO as GPIO
import time

import water_level

def ubeac(ultrasonic_sensor_in, ultrasonic_sensor_out, light, pump):
    while(True):
        data_waterlevel = water_level.depth_measurement(ultrasonic_sensor_in, ultrasonic_sensor_out)
        data_light = GPIO.input(light)
        data_pump = GPIO.input(pump)
        url = "http://emalisa.hub.ubeac.io/iotessEmalisa"
        uid = "iotessEmalisa"

        data= {
        "id": uid,
        "sensors":[{
            'id': 'waterlevel',
            'data': data_waterlevel
            },{
            'id': 'light',
            'data': data_light
            },{
            'id': 'pump',
            'data': data_pump
            }]
        }

        r = requests.post(url, verify=True,  json=data)

        time.sleep(1.5)
