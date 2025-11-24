import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"src=\"(\w+)\"",s)
    if match:
        return match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()
