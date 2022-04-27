import requests

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