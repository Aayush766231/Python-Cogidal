days = int(input("How many days? "))

years = days//365
weeks = (days%365)//7
daysNew = (days%365)%7

print(f"{years} years, {weeks} weeks, and {daysNew} days.")

