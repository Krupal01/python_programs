a1 = [1,2,5,3,2,5,1]
a2 = [8,8,4,5,7,5,6]

acon = a1 + a2
assending = []
decending = []

print("new array",acon)

while len(acon)>0:
    min = acon[0]
    for i in acon :
        if i < min :
            min = i
    assending.append(min)
    acon.remove(min)
print("assending",assending)

while len(assending)>0:
    max = assending[0]
    for i in assending :
        if i > max :
            max = i
    decending.append(max)
    assending.remove(max)
print("decending",decending)