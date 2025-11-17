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
                print(f"{prep[1]:02}/{months.index(prep[0].capitalize())}/{prep[2]}")
                return
            else:
                print(prep)
                return
        except:
            pass
main()
