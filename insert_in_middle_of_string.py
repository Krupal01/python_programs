a = "123456"

b = "xxx"
newstr = ""
i = int(len(a)/2)
print(i)
if len(a)%2==0:
    newstr = a[:i]+b+a[i:]

print(newstr)