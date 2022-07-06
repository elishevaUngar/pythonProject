# Exercise_5: 10 exercises
# sets
#1.(2). iteration over sets.
mySet = set([0, 1, 2, 3, 4])
for i in mySet:
    print(i, end=" ")
print("\nExercise_1: iteration over set:" , mySet)
#2.(3). add member(s) in a set.

mySet = set({1,2,3})
mySet.add("2")
print("Exercise_2: added value to set:" , mySet)

#3.(4). remove item(s) from a given set.
mySet = set({1,2,3})
mySet.remove(2)
print("Exercise_3: remove value from set:" , mySet)

#4.(5). remove an item from a set if it is present in the set.
mySet = set({1,2,3})
if 2 in mySet:
    mySet.remove(2)
print("Exercise_4: remove value from set if exist:" , mySet)

#5.(8). create set difference.
mySet1= set({1,2,3,9})
mySet2 = set({1,3,7,8})
print("Exercise_5: set difference:" , mySet1.difference(mySet2))

#6.(17). check if two given sets have no elements in common.
mySet1= set({1,2,3,9})
mySet2 = set({1,3,7,8})
print("Exercise_6: elements in common:" ,mySet1.isdisjoint(mySet2))

#7.(18). check if a given set is superset of itself and superset of another given set.
set1 = set({1,2,3,9})
set2 = set({2,3})
print("Exercise_7: is set2 is a superset of set2?" ,set1.issuperset(set2))

#8.(19). find the elements in a given set that are not in another set.
set1 = set({1,2,3,9})
set2 = set({1,3,7,8})
print("Exercise_8:" , set1.difference(set2), "from Set1 not in Set2")

#9.(20).remove the intersection of a 2nd set from the 1st set.
set1 = set({1,2,3,4})
set2 = set({3,4,5,6})
set1.intersection_update(set2)
print("Exercise_9:" ,set1 , "was removed")

#10 (11)  create a shallow copy of sets
set1 = set({1,2,3,4})
set2 = set1.copy()
print("Exercise_10:" ,set2 , "shallow copy")