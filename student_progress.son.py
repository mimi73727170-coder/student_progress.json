import json
student = {
    "name" : "Mimi",
    "course" : "Python",
    "Progress" : 25
}
with open("student.json","w") as file :
    json.dump(student,file)

print("Data saved!")

import json
with open("student.json","w") as file :
    json.dump(student,file)


with open("student.json","r") as file :
    data = json.load(file)

print(data)
print(data["name"])




print("MINI PROJECT")




student = {
    "name" : "Your name",
    "course" : "Python",
    "Progress" : 50
}
with open("student.json","w") as file :
    json.dump(student,file)

import json
with open("student.json","r") as file :
    data = json.load(file)

print(data)