s = input("Input: ")

v = ("A", "E", "I", "O", "U")

print("Output: ", end="")
for i in s:
    if i.upper() in v:
        print("",end="")
    else:
        print(i,end="")


