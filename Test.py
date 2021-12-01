import requests
import json
from datasender import *

with open('example.json') as json_file:
    data_toSend = json.load(json_file)

with open('example2.json') as json_file:
    data2 = json.load(json_file)

print(AddUpdate(123,data_toSend))
print(AddUpdate(456,data2))
#print(DispData())

