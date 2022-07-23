a = [1,2,3,6]

a1 = input("enter new element")
a1 = int(a1)
status = False
for i in range(0,len(a)):
    if a1<a[i]:
        a.insert(i, a1)
        status = True

if status == False:
    a.append(a1)

print(a)

