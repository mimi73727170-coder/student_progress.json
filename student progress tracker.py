students = {}

while True :
    print("\n1. Add Students")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter Choice :")

    if choice == "1" :
        name = input("Enter name :")
        progress = int(input("Enter progress :"))
         
        students[name] = progress
         
       

    elif choice == "2" :
        print(students)

    elif choice == "3" :
        break

    else :
        print("Invalid choice")

import json
with open ("students.json","w") as file :
    json.dump(students,file)
    
print("Data saved!")
