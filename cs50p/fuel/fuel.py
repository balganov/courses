

def main():
    print(get_fuel())

def get_fuel(left):
    l = left.split("/")
    result = int(round(int(l[0])/int(l[1])*100))

    while True
        try:
            fuel = input("Fraction: ")
            
            if result <= 1:
                return "E"
            elif result >= 99:
                return "F"
            else:
                return str(result) + "%"
        except (ValueError, ZeroDivisionError):
            pass

main()
