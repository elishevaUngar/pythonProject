# Exercise_1: 10 exercises
# 1. Write a Python program to import built-in array module and display the namespace of the said module.
import array


# for name in array.__dict__:
#   print(name)
# 2. Write a Python program to create a class and display the namespace of the said class.
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


print("2:")
for name in py_solution.__dict__:
    print(name)
# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance
print("3:")


class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


student = Student('123456789', 'Yossi', '35')
print(student.__dict__)
# 4.display the documentation of abs() function and find the absolute value of -155
print("4:")
import builtins

help(builtins.abs)  # documentation
print(builtins.abs(-155))  # apply the function abs
#5. Define a Python function student(). Using function attributes display the names of all arguments.
def printStudentDetails(id,name,age):
    return f'Student ID: {id} \nStudent Name: {name}\nStudent Age: {age}'
print(printStudentDetails("123456789","noam",23))
#6. Write a Python function student_data ()
# which will print the id of a student (student_id).
# If the user passes an argument student_name or student_class
# the function will print the student name and class.
print("6")
def printStudentDetails(id,**kwargs):
   print(f'Student ID: {id}')
   if(kwargs.__contains__('name')):
            print(f"Student Name: {kwargs['name']}\nStudent Age: {kwargs['age']}")
printStudentDetails("123456789",name="noam",age = 23)
#7.Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class
print("7")
class Student:
    pass
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)
#8. Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not
print("8")
class Student:
    pass
class Marks:
    pass
s = Student()
m = Marks()
print(isinstance(s, Student))
print(isinstance(m, Student))
print(isinstance(m, Marks))
#9.9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
print("9")
class Student:
    name = 'toni',
    mark = 76
print(f"Name: {getattr(Student, 'name')} Mark: {getattr(Student, 'mark')}")
setattr(Student, 'name', 'yoel')
setattr(Student, 'mark', 95)
print(f"Name: {getattr(Student, 'name')} Mark: {getattr(Student, 'mark')}")
#Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and their values of the said class. Now remove the student_name attribute and display the entire attribute with values.
# print("10")
class Student:
    name = 'toni',
    mark = 76
print(f"Name: {getattr(Student, 'name')} Mark: {getattr(Student, 'mark')}")
print("add a new attribute: age")
setattr(Student, 'age', 34)
print(f"Name: {getattr(Student, 'name')} Mark: {getattr(Student, 'mark')} Age: {getattr(Student, 'age')}")
print("delete name attribute: ")
delattr(Student, 'name')
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
#11.
print("11")
class Student:
    id = 1234
    name = 'toni'
    s_class='A'
    def display():
        for attr, value in Student.__dict__.items():
            if not attr.startswith('_'):
                print(f'{attr}: {value}')
Student.display()
#12
print("12")

class Student:
    school = 'Forward Thinking'
    address = '2626/Z Overlook Drive, COLUMBUS'
student1 =Student()
student2 = Student()
student1.elisheva = "89"
student1.id = "234"
student1.name = "tara"
student2.id = "567"
student2.marks_language = 78
student2.marks_science = 87
student2.marks_math = 90
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')

