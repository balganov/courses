import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    re.search(r"src=",s)

    return None

if __name__ == "__main__":
    main()
