def main():
    d = {}
    counter = 1
    while True:
        try:
            item = input()
            if item in d:
                d[item] += 1
            else:
                d[item] = counter
        except EOFError:
            print(d)
            return


if __name__ == "__main__":
    main()
