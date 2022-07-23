a = [1,2,3,4,5,6]

reverse = []

i = len(a)-1

while i>=0:
    reverse.append(a[i])
    i-=1

print(reverse)