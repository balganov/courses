

def main():


    while True:
        try:
            fuel = input("Fraction: ")
            print(how_much(fuel))
            return
        except (ValueError, ZeroDivisionError):
            pass
        except Exception:
            if fuel > 100:
                pass


def how_much(left):
    l = left.split("/")
    result = int(round(int(l[0])/int(l[1])*100))

    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return str(result) + "%"

main()
