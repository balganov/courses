import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^(\d|[0-1][0-2])(:[0-5]\d)? (A|P)M to (\d|[0-1][0-2])(:[0-5]\d)? (A|P)M$",s)
    if match:
        h1,m1,ampm1,h2,m2,ampm2 = match.groups()
        h1 = update24(h1,ampm1)
        h2 = update24(h2,ampm2)
        m1 = m1 or ':00'
        m2 = m1 or ':00'

        return f"{h1:02}{m1} to {h2:02}{m2}"
    else:
        raise ValueError

def update24(hs, ampm):
    h = int(hs)
    if ampm == 'P':
        return h if h == 12 else h + 12
    else:
        return 0 if h == 12 else h


if __name__ == "__main__":
    main()
