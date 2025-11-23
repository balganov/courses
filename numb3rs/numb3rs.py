import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^([0-2][0-5]{2}\.){3}[0-2][0-5]{2}$",ip)
    if match:
        print("Valid.")
        print(match.group())
    else:
        print("Invalid.")

...


if __name__ == "__main__":
    main()
