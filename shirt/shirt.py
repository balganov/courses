import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few comand-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many comand-line arguments")
    elif "." not in sys.argv[1]:
        sys.exit("Invalid input")
    elif sys.argv[1].lower().split(".")[1] not in ["jpeg","jpg","png"] or sys.argv[2].lower().split(".")[1] not in ["jpeg","jpg","png"]:
        sys.exit("Invalid output")
    elif sys.argv[1].lower().split(".")[1] != sys.argv[2].lower().split(".")[1]:
        sys.exit("Input and output have different extensions")
    else:
        input = sys.argv[1]
        output = sys.argv[2]
        try:
            shirt = Image.open("shirt.png")
            img_in = Image.open(input)
            resize = ImageOps.fit(img_in, size=[600,600])
            resize.paste(shirt, shirt)
            resize.save(output)
        except FileNotFoundError:
            sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
