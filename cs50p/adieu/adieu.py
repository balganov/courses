import inflect
p = inflect.engine()

def main():

    l = []

    try:
        while True:
            l.append(input("Name :" ))
    except EOFError:
            print("\nAdieu, adieu, to " + p.join((l)))

main()
