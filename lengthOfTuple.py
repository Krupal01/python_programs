
def Ispresent(array , object):
    if object in array:
        return True
    else :
        return False

def delet(a,index):
    a = list(a)
    a.pop(index)
    a = tuple(a)
    return a

def insret(a,index,object):
    a = list(a)
    a.insert(index, object)
    a = tuple(a)
    return a

def reverse(a):
    i = len(a)-1
    newa = []
    while i>=0:
        newa.append(a[i])
        i-=1
    a = tuple(newa)
    return a

def find_unique(a):
    unique = []
    for i in a:
        for j in a:
            if i == j:
                if j in unique:
                    break
                else:
                    unique.append(j)
    return unique

def find_duplicate(a):
    duplicate = []
    for i in a :
        count = 0
        for j in a :
            if i == j :
                count+=1
                if count==2 and Ispresent(duplicate, j)==False:
                    duplicate.append(j)
                    break
                
    return duplicate



a = (1,2,3,4,5,"dgg",6,6)
print(delet(a, 5))
print(insret(a, 6, "c"))
print(reverse(a))
print(find_duplicate(a))