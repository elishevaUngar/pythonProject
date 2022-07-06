import json

people_json = []

with open('example.json') as myJson:
    people_json = json.load(myJson)
    print(people_json["people"][1]["children"][0]["Age"])
    people_json["people"].append({"Name": "יוסי"})

print(people_json)

with open('example2.json', 'w') as myJson:
    json.dump(people_json, myJson, indent=4, sort_keys=True, ensure_ascii=False)


class Person:
    hasChildren = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi my name is {self.name}")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):

    def __init__(self, name, age='', course_name='', grade=100):
        super().__init__(name, age)
        self.course_name = course_name
        self.course_grade = grade

    def talk(self):
        print(f"Hi my name is {self.name} and my age is {self.age} ")

    def __dict__(self):
        return {'name': self.name, 'age': self.age, "class": self.__class__.__name__}


def encode_user(o):
    if isinstance(o, Person):
        return {'name': o.name, 'age': o.age, "class": o.__class__.__name__}
    else:
        raise TypeError("Object of type Person is not JSON serializable")


user1 = Person('Yuri', 31)
user2 = Person('Haim', 50)

student1 = Student('Yuri', 31, 'Advanced Python')

print(dir(student1))
student1.talk()

print(user1)
print(user1.hasChildren)
user1.talk()
user2.talk()

try:
    personJSON = json.dumps(student1, default=encode_user)
    print(personJSON)
except Exception as Error:
    print(Error)

print("Continuing... program")

from json import JSONEncoder


class PersonJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


personEncoded = PersonJsonEncoder().encode(student1)
print(type(personJSON))
print(str(personJSON))
print(type(abs))


# print(dict(user1))

# Next Topics:
# Random Numbers + a clips of numpy module
# Decorators
# Generators
# Threading vs Multiprocessing vs GIL
# Threading examples
# Multiprocessing example
# Async await syntax
