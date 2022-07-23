a = [1,2,5,3,6,9,5]
b = [1,2,9,6]

IsSubset = True

for i in b:
    if i in a:
        continue
    else :
        IsSubset = False
        break            

if IsSubset == False:
    print("No")
else:
    print("Yes")