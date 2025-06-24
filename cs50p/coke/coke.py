c = int(input("Insert Coin: "))
n = 0

while n < 50:
    if c == 25 or c == 10 or c == 5:
        n = n + c
        if 50 - n <= 0:
            print("Change Owed:", n - 50)
        else:
            print("Amount Due:", 50 - n)
            c = int(input("Insert Coin: "))
    else:
        print("Amount Due:", 50 - n)
        c = int(input("Insert Coin: "))


