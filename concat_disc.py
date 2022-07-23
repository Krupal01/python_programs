a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
b = {5: 49, 8: 64, 9: 81, 10: 100}

for key,value in b.items():
    if key in a.keys():
        print("not possible for key",key) 
    else:
        a[key]=value

print(a)