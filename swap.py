a = 5
b = 6
c = 7
d = 8

#with temp

temp = a
a = b
b = temp

print("a is ",a)
print("b is ",b)

#without temp

c = c+d
d = c-d
c = c-d

print("c is",c)
print("d is ",d)

