import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"^<iframe.+src=\"https?://(www\.)?youtube\.com/embed/(\S+)\"",s)
    if match:
        return f"https://youtu.be/{match.group(2)}"
    else:
        return None

if __name__ == "__main__":
    main()
