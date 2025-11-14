import random


def main():
    l = get_level()
    counter = 0
    errors = 0
    while counter < 10:
        first_int = generate_integer(l)
        second_int = generate_integer(l)
        sum = first_int + second_int
        while errors < 3:
            try:
                answer = int(input(f"{first_int} + {second_int} = "))
                if answer == sum:
                    counter += 1
                    break
                else:
                    print("EEE")
                    errors += 1
                    raise ValueError
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
