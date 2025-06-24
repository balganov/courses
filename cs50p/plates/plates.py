def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) <= 6 and s[-1].isdigit() and s.isalnum():
        return True
    else:
        return False

    for c in s:
        if c.isdigit():
            counter = counter + 1
            if c = 0 and counter = 1
                return False
            else:
                return True



main()
