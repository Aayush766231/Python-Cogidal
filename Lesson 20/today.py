from datetime import date, time, datetime

def month (currentMonth):
    if currentMonth == 1:
        return "January"
    elif currentMonth == 2:
        return "February"
    elif currentMonth == 3:
        return "March"
    elif currentMonth == 4:
        return "April"
    elif currentMonth == 5:
        return "May"
    elif currentMonth == 6:
        return "June"
    elif currentMonth == 7:
        return "July"
    elif currentMonth == 8:
        return "August"
    elif currentMonth == 9:
        return "September"
    elif currentMonth == 10:
        return "October"
    elif currentMonth == 11:
        return "November"
    else:
        return "December"

today = date.today()
now = datetime.now()

print(today)
print(now)

print("The year is", today.year, "the month is", month(today.month), "and the date is", today.day)
