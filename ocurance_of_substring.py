a = input("enter string : ")

len  = len(a)
count = 0

sub_len = 2

while sub_len<=len:
    count =count+(len-(sub_len-1))
    sub_len+=1

print(count)

