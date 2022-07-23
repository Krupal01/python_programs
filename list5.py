a = int(input("enter first number"))
b = int(input("enter last number"))
c = []

for i in range(a,b+1):
    if i<=a+5 or i>=b-5:
        c.append(i*i)

print(c)