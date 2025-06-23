def convert (phrase):
    phrase = phrase.replace(":)", "🙂").replace(":(", "🙁")
    return phrase;

def main():
    phrase = input()
    print(convert(phrase))

main()
