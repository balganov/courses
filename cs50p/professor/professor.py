import random


def main():
    l = get_level()
    counter = 10
    while counter < 10
        while True:
            try:
                answer = int(input((generate_integer(l) + "+" + generate_integer(l) + "=")
                                   
            except:
                continue


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
