#a program that checks which day of the week it is
#10/28/2022

from datetime import date
import time

weekdays = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}

action = str(input("If you want to know the day of the week, type: today, if you want to enter a different date, type: another: "))

if action == "today":
    timestamp = time.time()
    d = date.fromtimestamp(timestamp)
    print("Today is:",weekdays[d.isoweekday()])
elif action == "another":
    try:
        dat = str(input("Enter the date in the format YYYY-MM-DD: "))
        d = date.fromisoformat(dat)
        print("This day is:",weekdays[d.isoweekday()])
    except:
        print("The date entered is incorrect")
else:
    print("You have not selected an available option")

