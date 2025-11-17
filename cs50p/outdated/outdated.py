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
            prep = date.replace(",","").split()
            if prep[0].capitalize() in months:
                print("in list")
                return
            else:
                print(prep)
                return
        except:
            pass
main()
