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
        if date.split(" ").index(0) in months:
            print("here")
    except:
        pass
main()
