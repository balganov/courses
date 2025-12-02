import validators

def main():
    print("Valid") if validators.email(input("What's your email address? ")) else print("Invalid")

main()
