def main():
    d = {}
    counter = 1
    while True:
        try:
            item = input()
            if item.upper() in d:
                d[item.upper()] += 1
            else:
                d[item.upper()] = counter
        except EOFError:
            d = sorted(d.items())
            for key in d:
                print(f"{d[key]} {key}")
            return


if __name__ == "__main__":
    main()
