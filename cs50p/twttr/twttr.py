
def main():
    input = shorten(input("Input :"))
    print(f"Output: {input}")

def shorten(word):
    v = ("A", "E", "I", "O", "U")
    result = ""
    
    for i in word:
        if i.upper() in word:
            print("",end="")
        else:
            print(i,end="")

if __name__ = "__main__":
    main()
