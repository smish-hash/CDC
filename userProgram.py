from datasender import *

with open('Students.json') as json_file:
    dataToSend = json.load(json_file)

# Enter a user id in numerals, data as second argument of the AddUpdate function like AddUpdate(123,data_toSend)
clientId = 123
print(AddUpdate(clientId, dataToSend))

# to display dataset and delta, enter date in the following format - DispData(userid, "dd/mm/yyyy")
result = DispData(clientId, "02/11/2021")

loaded_file = open('resultFromTest.txt', 'w')
loaded_file.write(result)
loaded_file.close()

print(loaded_file)
