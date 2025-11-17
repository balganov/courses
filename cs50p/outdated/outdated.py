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
            if '/' in date and date[0].isdigit():
                prep = date.split("/")
                int_list = [int(s) for s in prep]
                if <= 1 int_list[0] <= 12 and 1 <= int_list[1] <= 31:
                    print(f"{prep[1]:02}-{prep[0]:02}-{prep[2]}")
                    return
                else:
                    print("here")
                    raise ValueError
            else:
                prep = date.replace(",","").split()
                if prep[0].capitalize() in months:
                    print(f"{prep[1]:02}-{months.index(prep[0].capitalize())+1:02}-{prep[2]}")
                    return
                else:
                    raise ValueError
        except:
            pass
main()
