assending = []
decending = []

aduplicate = [2,5,1,3,6,1,4]
a1 = [2,5,1,3,6,1,4,4]

#assending
while len(aduplicate)>0:
    min = aduplicate[0]
    for i in aduplicate :
        if i < min :
            min = i
    assending.append(min)
    aduplicate.remove(min)

print(assending)

#decending
while len(a1)>0:
    max = a1[0]
    for i in a1 :
        if i > max :
            max = i
    decending.append(max)
    a1.remove(max)

print(decending)    

    