import requests
import json
from datasender import *

with open('Students.json') as json_file:
    data_toSend = json.load(json_file)

#Enter a user id in numerals, data as second argument of the AddUpdate function like AddUpdate(123,data_toSend)
print(AddUpdate(123,data_toSend))

# For display of dataset and logs, enter in the following format - DispData(userid,"dd/mm/yyyy")
print(DispData(123,"02/11/2021"))

