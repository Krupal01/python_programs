#left rotate
a = [1,2,3,4,5]
n = input("enter number of step")
n1 = int(n)
n2 = int(n)
aleft = []
i = 0

if n1<=len(a):
    while n1<len(a):
        aleft.append(a[n1])
        n1 = n1+1
    while i<n2:
        aleft.append(a[i])
        i = i+1
else :
    print("your step is not valid")

print("left rotated array ",aleft)

#right roght

aright = []
n11 = int(n)
n12 = int(n)
j = 0

if n11<=len(a):
    while n11 <=len(a) :
        aright.append(a[n11-1])
        n11 = n11+1
    while j < n12-1:
        aright.append(a[j])
        j = j+1

else :
    print("your step is not valid")

print("right rotated array ",aright)
    