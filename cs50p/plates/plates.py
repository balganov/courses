def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) <= 6 and s.isalnum():
        digit_found = False
        for c in s:
            if c.isdigit():
                if not digit_found:
                    digit_found = True
                    if c == '0':
                        return False
        return True
    else:
        return False



main()
