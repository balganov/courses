def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) <= 6 and s[-1].isdigit() and s.isalnum():
        digit_found = False
        for c in s:
            if c.isdigit():
                digit_found = True
                if not digit_found and c == '0':
                    return False
        return True
    else:
        return False



main()
