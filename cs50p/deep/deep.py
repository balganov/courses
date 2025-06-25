

a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
check = a.strip().lower()

if check == "42" or check == "forty-two" or check == "forty two":
    print("Yes")
else:
    print("No")
