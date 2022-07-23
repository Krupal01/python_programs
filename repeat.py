a = [1,2,5,2,5,1,5,3]

while len(a)>0:
    count =0
    for j in a:
        if a[0]==j:
            count = count+1
    print(a[0],"-",count)
    z=a[0]
    while z in a : a.remove(z)