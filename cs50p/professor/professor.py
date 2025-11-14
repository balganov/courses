import random


def main():
    l = get_level()
    counter = 0
    score = 0
    while counter < 10:
        errors = 0
        first_int = generate_integer(l)
        second_int = generate_integer(l)
        sum = first_int + second_int
        while True:
            try:
                if errors == 3:
                    print(f"{first_int} + {second_int} = {sum}")
                    counter += 1
                    break
                answer = int(input(f"{first_int} + {second_int} = "))
                if answer == sum:
                    counter += 1
                    score += 1
                    break
                else:
                    print("EEE")
                    errors += 1
                    raise ValueError
            except:
                continue

    print(f"Score: {score}")

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
