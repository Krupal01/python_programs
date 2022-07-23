a = [1,2,3,4,2,1,5,4,3,2,1]

while len(a)>0:
    count = 0
    for i in a:
        if a[0]==i:
            count = count + 1
    if count>1: print(a[0])
    z = a[0]
    while z in a: a.remove(z)