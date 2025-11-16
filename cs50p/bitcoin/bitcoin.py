import sys
import requests


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():

    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit()
    elif not is_float(sys.argv[1]):
        print("Command-line argument is not a number")
        sys.exit()
    else:
        try:
            

main()
