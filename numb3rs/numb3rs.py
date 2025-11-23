import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^[0-9][0-9]?$",ip)
    if match:
        print("Valid.")
        print(match.group())
    else:
        print("Invalid.")

...


if __name__ == "__main__":
    main()
