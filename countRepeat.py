a = [1,2,5,6,3,3,2,1,2,2,4]

f = int(input("enter element"))

count = 0
for i in a:
    if i == f:
        count = count + 1

print(count)