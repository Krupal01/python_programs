a = [1,2,3,4,5,6]
b = ['a','b','c','d','e','f','g']

lenght = min(len(a), len(b))
disc = {}

for i in range(lenght):
    disc[a[i]] = b[i]

print(disc)


