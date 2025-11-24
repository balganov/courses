import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"src=\"(..*)\"",s):
        print()

    return None

if __name__ == "__main__":
    main()
