s = input("Input: ")

v = ("A", "E", "I", "O", "U")


for i in s:
    if i.upper in v:
        print("",end="")
    else:
        print(i,end="")


