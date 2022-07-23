def find_long(str):
    a = str.split(" ")
    max_len = 0
    max_word = " "
    for i in a:
        l = len(i)
        if max_len < l:
            max_len = l
    
    print("longest word length is :", max_len)

    for i in a:
        if len(i)==max_len:
            print("lognest word is :",i)


find_long("krupal is good person and he is real man")

