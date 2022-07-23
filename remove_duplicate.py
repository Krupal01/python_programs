a = [1,2,6,3,5,3,5]

i = 0
while i <len(a):
    j = 0
    while j <len(a):
        if i!=j and a[i]==a[j]:
            a.pop(j)
        j+=1
    i+=1

print(a)