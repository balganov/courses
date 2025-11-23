import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few comand-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many comand-line arguments")
    else:
        input = sys.argv[1]
        output = sys.argv[2]
        try:
            with open(input, "r") as file1, open(output, "w") as file2:
                fieldnames = ["first","last", "house"]
                reader = csv.DictReader(file1)
                writer = csv.DictWriter(file2, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    #print(row["name"].split(",")[1].split())
                    writer.writerow({"first": row["name"].split(",")[1].strip(),"last":row["name"].split(",")[0].strip(),"house":row["house"]})
        except FileNotFoundError:
            sys.exit(f"Couldn't read {sys.argv[1]}")

if __name__ == "__main__":
    main()
