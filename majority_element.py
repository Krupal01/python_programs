a = [1,2,5,6,3,5,2,8,8,8,5,5,5,2,8]

dic = {}

for i in a:
    count = 0
    for j in a :
        if i == j:
            count = count+1
    dic[i] = count 

max = 0
for i in dic.values():
    if i>max:
        max = i

for key , value in dic.items():
    if value == max:
        print(key)
    
