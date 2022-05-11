import requests
import RPi.GPIO as GPIO
import time

import water_level

def ubeac():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(5, GPIO.IN)
    GPIO.setup(12, GPIO.IN)

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

        # print(r)
        time.sleep(1)


def send_data_water(id_water, data_water, id_pump, data_pump):    
    url = "http://emalisa.hub.ubeac.io/iotessEmalisa"
    uid = "iotessEmalisa"
        
    data= {
    "id": uid,
    "sensors":[{
        'id': id_water,
        'data': data_water
        },{
        'id': id_pump,
        'data': data_pump
        }]
    }

    r = requests.post(url, verify=False,  json=data)

    print(r)