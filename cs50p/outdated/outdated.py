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

            if prep[0].capitalize() in months:
                prep = date.replace(",","").split()
                print(f"{prep[1]:02}/{months.index(prep[0])}/{prep[2]}")
                return
            else:
                print(prep)
                return
        except:
            pass
main()
