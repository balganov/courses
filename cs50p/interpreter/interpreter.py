s = input("Expression: ")

x,y,z = s.split(" ")

if y == "/":
    if z == "0":
        print("error")
    else:
        print(float(int(x)/int(z)))
elif y == "+":
    print(float(int(x)+int(z)))
elif y == "-":
    print(float(int(x)-int(z)))
else:
    print(float(int(x)*int(z)))

