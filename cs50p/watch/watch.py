import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"src=\"[https?](\S+)\"",s)
    if match:
        return f"https://youtu.be/{match.group(1).split("/")[4]}"
    else:
        return None

if __name__ == "__main__":
    main()
