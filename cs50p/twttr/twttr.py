s = input("Input: ")

v = ("A", "E", "I", "O", "U")


for i in v:
    if i in s:
        s.replace(i,"")
        print("here")

print("Output: ", s)
