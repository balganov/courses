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
            prep = date.replace(",","").capitalize().split()
            if prep[0] in months:
                print("in list")
                return
            else:
                print("else")
                return
        except:
            pass
main()
