# leap year check

year = int(input("Input a year: "))
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# month input 

month = int(input("Input a month 1-12: "))
if (month>= 1 and month <=12):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
else:
    print("Enter the vallid month")

# date inpute 

if month in (1, 3, 5, 7, 8, 10, 12):
    day = int(input("Input a day 1-31: "))
elif month in (4, 6, 9, 11):
    day = int(input("Input a day 1-30: "))
elif month ==(2):
    if leap_year:
        day = int(input("Input a day 1-29: "))
    else:
        day = int(input("Input a day 1-28: "))
if (day>= 1 and day <=31):
    pass
else:
    print("please enter valid date")
    exit()
# next date calculate

if((month == 1,3,5,7,8,10,12) and (day <= 31 and day >= 1)):
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
elif((month == 4,7,9,11) and (day <= 30 and day >=1)):
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
elif ( month == 2 ):
    if leap_year and (day <=29 and day >=1):
        if day < month_length:
            day += 1
        else:
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
    elif (day <=29 and day >=1):
        if leap_year and (day <=29 and day >=1):
            if day < month_length:
                day += 1
            else:
                day = 1
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
    else:
        print("please enter valid date")
print("The next date is %d-%d-%d." % (day, month, year,))




