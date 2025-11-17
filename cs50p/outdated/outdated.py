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

    try:
        date = input("Date: ")
        print(date.split(" ").index(0))
    except:
        pass
main()
