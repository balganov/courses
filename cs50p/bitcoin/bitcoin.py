import sys
import requests
import json


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
            r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=e8d5c419eda93141a0fc9a8b0c95192a27c9105f9df50d8435e1c891135b9bf9')
            response = r.json()
            print(response(["data"]))
        except requests.RequestException as e:
            print(e)

main()
