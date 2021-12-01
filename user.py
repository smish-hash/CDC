import FlaskTest as ft
import json

print("Hello this is user")

f = open('Students.json')

# dict type
db = json.load(f)
students = []

for key, value in db.items():
    if key == 'Students':
        students = value

for key in students[0].keys():
    print(key)

ft.getCharacters(students)




