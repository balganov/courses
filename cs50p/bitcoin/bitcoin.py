import sys
import requests

def main():

    if len(sys.argv) == 1:
        print("Missing command-line argument\n")
        sys.exit()
    elif float(sys.argv[1]) is False:
        print("Command-line argument is not a number\n")
        sys.exit()
    else:
        print("all good")
        sys.exit()

main()
