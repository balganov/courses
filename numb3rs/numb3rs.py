import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^0-255{3}\.{3}\.{3}\.{3}$",ip)


...


if __name__ == "__main__":
    main()
