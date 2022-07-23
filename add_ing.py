a = "add sleep sing ask is"

""" Write a Python program to add 'ing' at the end of a givenstring
(length should be at least 3). If the given string already ends with
 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave itunchanged """

for i in a.split(" "):
    if len(i)>=3:
        j = len(i)-3
        if i[j:] == "ing":
            i = i[:j]+"ly"            
        else:
            i = i+"ing"
        print(i)
    else:
        print(i)
