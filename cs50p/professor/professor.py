import random


def main():
    print(get_level())
    print(generate_integer(get_level()))


def get_level():
    try:
        while True:
            level = int(input("Level: "))
            if level < 4 or level > 0:
                return level
            else:
                raise ValueError
    except:
        continue


def generate_integer(level):
    


if __name__ == "__main__":
    main()
