# Exercise_1: 10 exercises
# Lists
# 1.sum all the items in a list
myList = [1, 2, 3]
count = 0
for num in myList:
    count += num
print("Exercise_1: the sum of all list is:" + str(count))
# 2.multiply all the items in a list
count = 1
for num in myList:
    count *= num
print("Exercise_2: the multiplication of all list is:" + str(count))
# 3. (10) find the list of words that are longer than n from a given list of words
n = 4
wordList = ["i", "iona", "elisheva", "simcha"]
longerWords = []
for word in wordList:
    if len(word) > n:
        longerWords.append(word)
print("Exercise_3: list of words that are longer than n " + str(longerWords))
# 4.11 takes two lists and returns True if they have at least one common member
list1 = [1, 2, 3, 6]
list2 = [3, 4, 5]
if len([x for x in list1 if x in list2]) > 0:
    print("Exercise_4: there are common member in the lists, response: true")

# 5.22 to find the index of an item in a specified list
list1 = [1, 2, 3, 4]
print("Exercise_5: item 3 founded in specified List at index: " + str(list1.index(3)))


# 6.count the number of elements in a list within a specified range
def countElementInRange(list, minR, maxR):
    index = 0
    counter = 0
    for item in list:
        if index >= minR and index <= maxR:
            counter += 1
        index += 1
    return counter


print("Exercise_6: there are " + str(
    countElementInRange([1, 2, 3, 4, 5, 6, 7], 1, 2)) + " item in chosen range of this list: ", [1, 2, 3, 4, 5, 6, 7])


# 7.260. check if all the elements of a list are included in another given list.
def isListIncluded(list1, list2):
    counter = 0
    for x in list1:
        if x in list2:
            counter += 1
        if counter == len(list1):
            return "true"
    return "false"
print("Exercise_7.1:" + isListIncluded([1, 2, 3, 4, 5,6], [1, 2, 3, 4, 5]))
# better way
def isListIncluded1(list1, list2):
    for x in list1:
        if x not in list2:
            return "false"
    return "true"
print("Exercise_7.2: "+ isListIncluded1([1, 2, 3, 4, 5,6], [1, 2, 3, 4, 5]))

#8.253 n minimum elements from a given list of number
list1 = [10,21,-3,4,6,5,3,4]
list1.sort()
print("Exercise_8: 3 minimum elements",list1[:3])

#9.261. get the most frequent element in a given list of numbers
list1 = [1,2,3,4,3,3,2,3]
print("Exercise_9: the most frequent element", max(set(list1), key=list1.count))

#10.271.check if there are duplicate values in a given flat list
tempList = []
for x in list1:
    if x not in tempList:
        tempList.append(x)
if len(tempList) > 0:
    print("Exercise_10: there are",len(tempList), "duplicate value in list")
else:
    print("Exercise_10: none duplicate values")