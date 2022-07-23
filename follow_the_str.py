a = "krupal is not poor and he is poor and not"

asplit = a.split(" ")

len = len(asplit) - 2

for i in range(len):
    if asplit[i] == "not":
        if asplit[i+1] == "poor":
            asplit[i] = "good"
            asplit.pop(i+1)
             
print(asplit)



