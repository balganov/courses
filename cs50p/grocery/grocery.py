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
            sorted_items = sorted(d.items())
            sorted_dict = dict(sorted_items)
            for key in sorted_dict:
                print(f"{d[key]} {key}")
            return


if __name__ == "__main__":
    main()
