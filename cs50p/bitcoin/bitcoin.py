import sys
import requests


def is_float(value):
    if float(value): return True else: return False


def main():

    if len(sys.argv) == 1:
        print("Missing command-line argument\n")
        sys.exit()
    elif float(sys.argv[1]):
        print("Command-line argument is not a number\n")
        sys.exit()
    else:
        print("all good")
        sys.exit()

main()
