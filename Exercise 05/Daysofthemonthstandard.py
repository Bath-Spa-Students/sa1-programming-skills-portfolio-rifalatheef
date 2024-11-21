"""Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly."""

#make a dictionary
Number_of_days = {
# January
    1:31,
    # February
    2:28,
    # March
    3:31,
    # April
    4:30,
    # May
    5:31,
    # June
    6:30,
    # July
    7:31,
    # August 
    8:31,
    # September
    9:30,
    # October
    10:31,
    # November
    11:30,
    # December
    12:31,

}


# asking the user for the month number.
month_number = int(input("Type the month number:"))

#check the month and printing the numbers of days
if 1 <=month_number <=12:
    print(f"The number of days in month {month_number} is {Number_of_days[month_number]}")
else:
    print("Invaild month number!")

