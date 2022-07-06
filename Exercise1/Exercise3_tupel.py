# Exercise_3 : 5 exercises
# tuple
#1. create a tuple.
tuple = (1,2,3,4,5)
print("Exercise_1: create a tuple: " ,tuple)
#2. create a tuple with different data types.
tuple = (1,2,-3,4.3,"five")
print("Exercise_2: create a tuple with different types: " ,tuple)

#3. create a tuple with numbers and print one item.
tuple = (1,2,3,4,5)
print("Exercise_3: print one item: " ,tuple[0])

#4. unpack a tuple in several variables.
tuple = (1,2,3)
x1, x2, x3 = tuple
print("Exercise_4: tuple:",tuple," unpack variable:",x1 + x2 + x3)

#5. add an item in a tuple.
tuple = tuple + (6,7,8)
print("Exercise_5: add (6,7,8) to tuple (1,2,3,4,5): " ,tuple)
