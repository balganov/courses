

def main():
    fuel = input("Fraction: ")
    print(how_much(fuel))


def how_much(left):
    l = left.split("/")
    result = int(l[0])/int(l[1])*100
    return result + "%"

main()
