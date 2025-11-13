import random

def main():

    while True:
        try:
            level = int(input("Level: "))
            if level < 0: raise ValueError()
            break
        except:
            continue

    num = random.randint(1,level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if(guess == num):
                    print ("Just right!")
                    break
                elif (guess < num):
                    print ("Too small!")
                else:
                    print ("Too large!")
            else:
                raise ValueError()
        except:
            continue

main()
