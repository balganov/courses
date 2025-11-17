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
            for key in d:
                print(f"{d[key]} {d.value(key)}\n")
            return


if __name__ == "__main__":
    main()
