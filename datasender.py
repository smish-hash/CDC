import requests
import json
from datetime import datetime


def AddUpdate(clientId, dataa):
    data_endpoint = "http://127.0.0.1:5000/database"

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    dta = {'clientid': clientId, 'timestamp': timestamp, 'data': dataa, 'dateTime': now.strftime("%m/%d/%Y, %H:%M:%S")}
    dta = json.dumps(dta)

    resp = requests.post(url=data_endpoint, data=dta)

    if resp.status_code == 200:
        return json.dumps((eval(resp.text)), indent=4, sort_keys=True)
    else:
        return "Your api has some problem. Status" + str(resp.status_code)


def DispData(userid, caldate):
    data_endpoint = "http://127.0.0.1:5000/clientcall"

    element = datetime.strptime(caldate, "%d/%m/%Y")
    caltimestamp = datetime.timestamp(element)
    dataList = [userid, caltimestamp]
    data = json.dumps(dataList)

    resp = requests.post(url=data_endpoint, data=data)

    if resp.status_code == 200:
        return json.dumps((eval(resp.text)), indent=4, sort_keys=True)
    else:
        return "Your api has some problem. Status" + str(resp.status_code)
