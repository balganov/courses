import inflect
from datetime import date
import sys

def main():
    print(minutes(input("Date of Birth: ")))

def minutes(birthday):
    try:
        p = inflect.engine()
        bd = date.fromisoformat(birthday)
        dif = date.today() - bd
        return f"{p.number_to_words(dif.days*24*60, andword="").capitalize()} minutes"
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
