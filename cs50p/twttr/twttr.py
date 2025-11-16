
def main():
    result = shorten(input("Input :"))
    print(f"Output: {result}")

def shorten(word):
    v = ("A", "E", "I", "O", "U")

    for i in word:
        if i.upper() in v:
            print("",end="")
        else:
            print(i,end="")

if __name__ = "__main__":
    main()
