import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5]{2})\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5]{2})$",ip):
        print(match.group(0),match.group(1),match.group(2),match.group(3))
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
