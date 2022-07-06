# Exercise_7 : 3 exercises
# lambda
#1.a create a lambda function that adds 15 to a given number passed in as an argument

a= lambda a: a+15
print("Exercise_1.a: adds 15 to a given number:",a(5))
#1.b create a lambda function that multiplies argument x with argument y and print the result.

a = lambda x,y: x * y
print("Exercise_1.b: multiplies x with y :",a(5,6))

#2. sort a list of dictionaries using Lambda
listOfDic=[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
           {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Exercise_2: sorted list of dictionaries by lambda",sorted(listOfDic, key = lambda x: x['color']))

#3.filter a list of integers using Lambda
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Exercise_3.a: filter list by even number:",list(filter(lambda n: n%2==0,numlist)))
print("Exercise_3.b: filter list by ood number:",list(filter(lambda n: n%2!=0,numlist)))
