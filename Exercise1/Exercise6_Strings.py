# Exercise_6 : 3-7 exercises
# strings
#1.calculate the length of a string.
s ="elisheva"
print("Exercise_1: The length of elisheva is:",len(s))

#2.count the number of characters
sentence= "elisheva"
tempDic={}
for ch in sentence:
    if ch not in tempDic:
        tempDic[ch] = sentence.count(ch)
print("Exercise_2: The count of characters in 'elisheva' is:", tempDic)
#3.(4).get a string from a given string where all occurrences of its first char have been changed to '$'

sentence = "elisheva"
print("Exercise_3: all occurrences of e in 'elisheva' was changed to $:",sentence[0] + sentence.replace(sentence[0],"$")[1:])

#4. (13) takes input from the user and displays that input back in upper and lower cases
sentence = "elisheva"
print("Exercise_4: upper and lower cases: upper:",sentence.upper(),"lower:",sentence.lower())

#5. (14) create the HTML string with tags around the word(s)
sentence = "elisheva"
print("Exercise_5: HTML string ","<%s>%s</%s>" % ('i',sentence, 'i'),"<%s>%s</%s>" % ('b',sentence, 'b'))