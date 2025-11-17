def main():
    months = ["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

    while True:
        try:
            date = input("Date: ")
            r = date.replace(",","")
            if date.split(" ")[0] in months:
                print("asdasd")
                return
            else:
                print("else")
                return
        except:
            pass
main()
