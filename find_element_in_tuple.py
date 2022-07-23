a = (1,2,3,4,5,6)

x = int(input("enter element"))
IsPresent = False

for i in a:
    if i == x:
        IsPresent = True

if IsPresent:
    print("present")
else :
    print("absent")