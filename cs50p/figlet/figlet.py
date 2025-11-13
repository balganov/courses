from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():

    if (len(sys.argv) == 1):
        text = input("Input: ")
        f = random.choice(figlet.getFonts())
        figlet.setFont(font = f)
        print("Output: \n" + figlet.renderText(text))
    elif (len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font") and (sys.agrv[2] in i for i in figlet.getFonts())):
        text = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print("Output: \n" + figlet.renderText(text))
    else:
        sys.exit("Invalid usage")

main()
