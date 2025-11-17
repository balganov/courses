def main():
    fuel = input("Fraction: ")
    print(gauge(convert(fuel)))

def convert(fraction):
    l = fraction.split("/")
    return int(round(int(l[0])/int(l[1])*100))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage > 100:
        raise Exception()
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

