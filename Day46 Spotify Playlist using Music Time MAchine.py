import datetime as dt

curr_date = dt.datetime.now().date()


def valid_date_checker(date):
    split_date = date.split("-")
    # if split_date[1][0]=="0":
    #     split_date[1]=split_date[1][1]
    # if split_date[2][0]=="0":
    #     split_date[2]=split_date[2][1]
    if (
        int(split_date[0]) <= curr_date.year
        and 0 < int(split_date[2]) <= 31
        and 0 < int(split_date[1]) <= 12
        and int(split_date[1]) <= curr_date.month
        and int(split_date[2]) <= curr_date.day
    ):
        return date
    else:
        print(end="\033c")
        print("Invalid date!! Enter Valid date")
        valid_date_checker(
            input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
        )


print(valid_date_checker(input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")))
