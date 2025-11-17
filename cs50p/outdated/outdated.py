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
            if date.split(" ")[0] in months:
                result = date.replace(",","").split(" ")
            return
        except:
            pass
main()
