
def reverse(str):
    l1 = len(str)-1
    c = ""
    while l1>=0:
        c = c+str[l1]
        l1-=1
    
    return c

a = "abcdefghijk"

if len(a)%4 == 0:
    print(reverse(a))
else:
    print("not possible")