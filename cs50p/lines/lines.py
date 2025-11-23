import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few comand-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments")
    elif sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a Python file")
    else:
        filename = sys.argv[1]
        clean = []
        try:
            with open(filename, "r") as file:
                for row in file:
                    if not (row.lstrip().startswith("#") or row.strip() == ''):
                        clean.append(row.strip())
                print(len(clean))
        except FileNotFoundError:
            print("File does not exist")

if __name__ == "__main__":
    main()
