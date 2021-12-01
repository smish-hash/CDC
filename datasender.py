import requests
import json
from datetime import datetime

def AddUpdate(id,dataa):
    data_endpoint = "http://127.0.0.1:5000/database"
    now=datetime.now()
    timestamp=datetime.timestamp(now)
    #print(timestamp)
    dta={'clientid':id, 'timestamp':timestamp, 'data':dataa}
    dta = json.dumps(dta)
    #print(type(dataa))
    #print(type(dta))
    resp = requests.post(url=data_endpoint, data=dta)
    if resp.status_code == 200:
        return eval(resp.text)
    else:
        return "Your api has some problem. Status" + str(resp.status_code)

def DispData():
    data_endpoint = "http://127.0.0.1:5000/database"
    resp = requests.get(url=data_endpoint)
    return eval(resp.text)