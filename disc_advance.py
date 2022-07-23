def getkey(array,value):
    for key,val in array.items():
        if value in val:
            return key

disc = {'1':['a','b'], '2':['c','d']}

for i in disc.keys():
    a = disc[i]
    b = disc.values()
    for j in a :
        for k in b:
            for m in k:
                if getkey(disc, j) != getkey(disc, m):
                    print(j,m)
    
