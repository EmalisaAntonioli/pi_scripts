import requests
import RPi.GPIO as GPIO
import time

import water_level

def ubeac():
    while(True):
        data_waterlevel = water_level.depth_measurement(26, 19)
        data_light = GPIO.input(5)
        data_pump = GPIO.input(12)
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

        r = requests.post(url, verify=False,  json=data)

        time.sleep(1)
