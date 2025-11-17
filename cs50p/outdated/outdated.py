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
            date = input("Date: ").strip()
            if '/' in date and date[0].isdigit():
                prep = date.split("/")
                int_list = [int(s) for s in prep]
                if 1 <= int_list[0] <= 12 and 1 <= int_list[1] <= 31 and 1000 <= int_list[2] <= 9999:
                    print(f"{int_list[2]:04d}-{int_list[0]:02d}-{int_list[1]:02d}")
                    return
                else:
                    raise ValueError
            else:
                if ',' not in date and prep[0].capitalize() in months:
                    prep = date.replace(",","").split()
                    prep[0] = months.index(prep[0].capitalize())+1
                    print(prep)
                    int_list = [int(s) for s in prep]
                    if 1 <= int_list[0] <= 12 and 1 <= int_list[1] <= 31 and 1000 <= int_list[2] <= 9999:
                        print(f"{int_list[2]:04d}-{int_list[0]:02d}-{int_list[1]:02d}")
                        return
                else:
                    raise ValueError
        except:
            pass
main()
