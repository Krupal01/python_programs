
def getkey(disc,value):
    for key,val in disc.items():
        if val == value:
            return key

a = {"a":1,"b":2,"c":3,"d":4,"e":5}

#assending order
assending_sort = {}
i = 1
while i <= len(a):
    m = min(a.values())
    key = getkey(a, m)
    assending_sort[key]=m
    del a[key]

print(assending_sort)


#decending order
decending_sort = {}
j = 1
while j <= len(assending_sort):
    m = max(assending_sort.values())
    key = getkey(assending_sort, m)
    decending_sort[key] = m
    del assending_sort[key]

print(decending_sort)

    

 