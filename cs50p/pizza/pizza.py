import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few comand-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments")
    elif sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")
    else:
        filename = sys.argv[1]
        clean = []
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    clean.append(row)
            #print(clean)
            print(tabulate(clean, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()
