a = [1,2,3,4,5,6]

i = 0

odd = []
even = []

while i<len(a):
    if (i+1)%2 == 0 :
        even.append(a[i])
    else:
        odd.append(a[i])
    i+=1

print("odd" , end=" ")
for j in odd : print(j , end=" ")
print(" ")
print("even" , end=" ")
for j in even : print(j , end=" ")