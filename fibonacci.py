def fibonnaci(len):
    count = 2
    a = 1
    b = 1
    print(a , end=" ")
    print(b , end=" ")
    while count<len:
        c = a+b
        print(c , end=" ")
        a = b
        b = c
        count+=1

length = int(input("enter length of fibonnaci series"))
fibonnaci(length)
