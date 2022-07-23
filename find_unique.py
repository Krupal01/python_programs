def unique(a):
    i = 0
    while i<len(a):
        j = 0
        while j<len(a):
            if a[i] == a[j] and i!=j:
                a.pop(j)
            j+=1
        i+=1
    return a

a = [1,2,3,5,3,2]
print(unique(a))