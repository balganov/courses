
def main():
    result = shorten(input("Input : "))
    print(f"Output: {result}")

def shorten(word):
    v = ("A", "E", "I", "O", "U")
    new_word = ""
    for i in word:
        if not i in v:
            new_word += i

    return new_word

if __name__ == "__main__":
    main()
