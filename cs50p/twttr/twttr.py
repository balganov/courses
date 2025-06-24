s = input("Input: ")

v = ("A", "E", "I", "O", "U")



for c in s:
    if c.upper in v:
        s.replace(c,"")
        print("here")

print("Output: ", s)
