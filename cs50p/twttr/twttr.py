s = input("Input: ")

v = ("A", "E", "I", "O", "U")


for c in s:
    for c in v:
        s.replace(c,"")
        print("here")

print("Output: ", s)
