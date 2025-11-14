import random


def main():
    print(get_level())
    print(generate_integer(get_level()))


def get_level():
    while True:
            try:
                level = int(input("Level: "))
                if level > 0 and level < 4:
                    return level
                    break
                else:
                    raise ValueError
            except:
                continue


def generate_integer(level):
    if level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
