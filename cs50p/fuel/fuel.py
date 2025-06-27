

def main():
    print(get_fuel())

def get_fuel():
    while True:
        try:
            l = input("Fraction: ").split("/")
            result = int(round(int(l[0])/int(l[1])*100))

            if result <= 1:
                print("E")
            elif result > 100:
                raise Exception()
            elif result >= 99:
                print("F")
            else:
                print(str(result) + "%")
        except (ValueError, ZeroDivisionError):
            pass

main()
