import requests
import json
import time
from datetime import datetime


def AddUpdate(id, dataa):
    data_endpoint = "http://127.0.0.1:5000/database"
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # 1577971124.673931
    # print(timestamp)
    dta = {'clientid': id, 'timestamp': timestamp, 'data': dataa, 'dateTime': now.strftime("%m/%d/%Y, %H:%M:%S")}
    dta = json.dumps(dta)
    # print(type(dataa))
    # print(type(dta))
    resp = requests.post(url=data_endpoint, data=dta)
    if resp.status_code == 200:
        return (json.dumps((eval(resp.text)), indent=4, sort_keys=True))
    else:
        return "Your api has some problem. Status" + str(resp.status_code)


# def DispData(userid,caldate):
#     data_endpoint = "http://127.0.0.1:5000/database"
#     element = datetime.strptime(caldate,"%d/%m/%Y")
#     caltimestamp = datetime.timestamp(element)
#     lst1=[userid,caltimestamp]
#     resp = requests.get(url=data_endpoint,data=lst1)
#     return eval(resp.text)



def DispData(userid,caldate):
    data_endpoint = "http://127.0.0.1:5000/clientcall"
    element = datetime.strptime(caldate,"%d/%m/%Y")
    caltimestamp = datetime.timestamp(element)
    lst1=[userid,caltimestamp]
    data = json.dumps(lst1)
    # print(data)
    # print(type(data))
    resp = requests.post(url=data_endpoint, data=data)
    if resp.status_code == 200:
        return (json.dumps((eval(resp.text)), indent=4, sort_keys=True))
    else:
        return "Your api has some problem. Status" + str(resp.status_code)
