import requests
import json

def AddUpdate(dataa):
    data_endpoint = "http://127.0.0.1:5000/database"
    dataa = json.dumps(dataa)
    resp = requests.post(url=data_endpoint, data=dataa)
    if resp.status_code == 200:
        return eval(resp.text)
    else:
        return "Your api has some problem. Status" + str(resp.status_code)

def DispData():
    data_endpoint = "http://127.0.0.1:5000/database"
    resp = requests.get(url=data_endpoint)
    return eval(resp.text)