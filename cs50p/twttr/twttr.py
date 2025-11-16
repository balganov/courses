
def main():
    result = shorten(input("Input : "))
    print(f"Output: {result}")

def shorten(word):
    v = ("A", "E", "I", "O", "U")
    for i in word:
        if i.upper() in v:
            word.replace(i,"")

    return word

if __name__ == "__main__":
    main()
