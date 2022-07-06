# Exercise_2 : 8 exercises
# Dictionary
# 1.(2) Write a Python script to add a key to a dictionary
personDic = {"Name": "David", "Age": 20}
personDic.update({"Gender":"man"})
print("Exercise_1: Gender added to the dictionary", personDic)
#2.(3)concatenate following dictionaries to create a new one
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic3.update(dic1)
dic3.update(dic2)
print("Exercise_2: concatenate dictionary", dic3)
#3.(4) check whether a given key already exists in a dictionary.
dic1 = {"Name": "David", "Age": 20}
if "Name" in dic1:
  print("Exercise_3: The Key already exist")
#4.(6) generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
dic = {}
n = 5
for i in range(1, n + 1):
    dic[i] = i * i
print("Exercise_4: dictionary contains number in form X,X*X",dic)
#5.(7).print a dictionary where the keys are numbers between 1 and 15 values are square of keys

dic = {}
for i in range(1,16):
    dic[i] = i**2
print("Exercise_5: dictionary contains number in form X,X^2", dic)
#6.(12) remove a key from a dictionary
personDic.pop("Age")
print("Exercise_6: the key age was removed from dic", personDic)
#7.(15). get the maximum and minimum value in a dictionary
dic2 = {3:30, 4:40, 5:50}
print("Exercise_7: max in dic is:", max(dic2), "the min is:",min(dic2))
#8. (19). combine two dictionary adding values for common keys.
dic1 = {"a":100,"b":200}
dic2 = {"a":300,"b":400}
counter ={}
for key in dic1:
    if key in dic2:
        counter.update({key:dic1[key]+dic2[key]})
print("Exercise_8: combine two dictionary:" ,(counter))

