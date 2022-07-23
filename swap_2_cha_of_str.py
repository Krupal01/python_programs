a = "krupal is student"
b = "krupal is engineer"

c = a+" "+b
print(c)

print(c.split(" "))

for i in c.split(" "):
    if len(i)>=2:
        new  = i[1]+i[0]+i[2:]
        print(new)
    

# swap first 2 characteer of one string to first 2 character of another string

a = "abc"
b = "xyz"

c = a[:2]+b[2:]+" "+b[:2]+a[2:]
print(c)