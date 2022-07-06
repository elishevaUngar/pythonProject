# Exercise_4 : 2 exercises
# collection
from collections import Counter

#1.iterate over elements repeating each as many times as its count.
col = Counter(a=2, b=4, c=6)
print(list(col.elements()))


#2. find the most common elements and their counts of a specified text.
def MostCommon(str,topX):
    return Counter(str).most_common(topX)
print(MostCommon("elisheva",3))
