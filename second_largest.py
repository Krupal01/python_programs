a = [1,2,5,6,3,5,7,8]


#second largest
for i in range(0,2):
    max = 0
    for j in a:
        if j > max:
            max = j
    while max in a: a.remove(max)

print(max)

#second smallest
for i in range(0,2):
    min = a[0]
    for j in a:
        if j < min:
            min = j
    while min in a: a.remove(min)

print(min)