import re

def main():
    print(count(input("Text: ")))


def count(s):
    find_um = re.findall(r"\bum\b",s.lower())
    return len(find_um)

if __name__ == "__main__":
    main()
