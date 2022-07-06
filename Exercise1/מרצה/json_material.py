# JSON - Javascript Object Notation
# {
#     "people" : [
#         {
#             "Name": "Yuri",
#             "Age" : 31
#         },
#         {
#             "Name": "Haim",
#             "Age": 50
#         }
#     ]
# }

# XML - Extended Markup Language
# XAML - Extended Applicative Markup Language
# <People>
#     <Person>
#         <Name>Yuri</Name>
#         <Age>31</Age>
#     </Person>
#     <Person>
#         <Name>Haim</Name>
#         <Age>50</Age>
#     </Person>
# </People>
import json

people_json = []

with open('../../Contacts/ContactData.json') as myJson:
    # people_json = json.loads(myJson.read())
    people_json = json.load(myJson)
    print(people_json["people"][1]["children"][0]["Age"])
    people_json["people"].append({"Name":"יוסי"})



print(people_json)

with open('example2.json','w') as myJson:
    json.dump(people_json,myJson,indent=4,sort_keys=True,ensure_ascii=False)



class Person:
    hasChildren = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

user1 = Person('Yuri', 31)

print(user1)
print(user1.hasChildren)

# print(type(abs))