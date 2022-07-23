b = {5: 49, 8: 64, 9: 81, 10: 100}

key = int(input("enter key"))

IsPresent = False
for keys in b.keys():
    if key == keys:
        IsPresent = True

if IsPresent == True:
    print("yes")
else :
    print("no")