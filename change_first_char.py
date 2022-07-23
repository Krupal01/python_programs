a = "krupalkfdfgk"

#A2.Write a Python program to get a string from a given string where all occurrences 
# of its first char have been changed to '$', except the first charitself
newstr = ""
for i in range(len(a)):
    if i!=0 and a[i]==a[0]:
        newstr = newstr+"$"
    else:
        newstr = newstr+a[i]     

print(newstr)


    

