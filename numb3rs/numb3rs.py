import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5]{2})\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5]{2})$",ip)
    if match:
        print("Valid.")
        print(match.group())
    else:
        print("Invalid.")

...


if __name__ == "__main__":
    main()
