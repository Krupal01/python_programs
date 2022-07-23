def IsCommon(a,b):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False

a = [1,2,3,4,5]
b = [6,7,8,1,9]

if(IsCommon(a, b)):
    print("yes")
else:
    print("no")

