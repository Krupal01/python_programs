a = [2,3,6,5,-6,-7]

while True:
    min1 = min(a)
    if min1 >= 0 :
        print(min1)
        break
    else:
        a.remove(min1)
