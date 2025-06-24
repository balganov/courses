def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) <= 6 and s[-1].isdigit() and s.isalnum():
        for c in s:
            if c.isdigit():
                if c == '0':
                    return False
            else:
                return True
    else:
        return False



main()
