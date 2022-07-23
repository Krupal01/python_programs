a = [1,2,3,0,4,7,5,6]

max = 0
min = a[-1]

for i in a :
    if i <min :
        min = i

    if i>max:
        max = i

print("min",min)
print("max",max) 