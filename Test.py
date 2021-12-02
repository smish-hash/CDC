from datasender import *

with open('Students.json') as json_file:
    data_toSend = json.load(json_file)

print(AddUpdate(567, data_toSend))
print(DispData())
