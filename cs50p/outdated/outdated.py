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
            if date[0].isnumeric():
                prep = date.split("/")
                if prep[0] <= 12 or prep[1] <= 31:
                    print(f"{prep[1]:02}-{prep[0]:02}-{prep[2]}")
                    return
                else:
                    raise ValueError
            else:
                prep = date.replace(",","").split()
                if prep[0].capitalize() in months:
                    print(f"{prep[1]:02}-{months.index(prep[0].capitalize())}-{prep[2]}")
                    return
                else:
                    raise ValueError
        except:
            pass
main()
