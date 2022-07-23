a = [1,1,2,3,4,5,6,5]

for i in a:
    count = 0
    for j in a:
        if i == j:
            count = count+1
    if count == 1:
        print(i,end=" ")