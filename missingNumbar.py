a = [1,2,3,4,6,7,9]

max = 0
for i in a:
    if i > max:
        max = i

for j in range(1,max+1):
    if j in a : 
        continue
    else : print(j)
        
