
def main():
    t = input("What time is it?: ")
    f = convert(t)
    if 7 <= f <= 8:
        print("breakfast time")
    elif 12 <= f <= 13:
        print("lunch time")
    elif 18 <= f <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    return float(int(hours)+int(minutes)/60)

if __name__ == "__main__":
    main()
