age = int(input("How old are you? "))
grade = int(input("What grade are you in? "))

if grade == 10:
    if age >= 10 and age <= 20:
        print("You are enrolled in the class. ")
    else:
        print("You are not enrolled.")
else:
    if grade > 10:
        print("You can't learn anything from this class")
    else:
        print(10 - grade, "years to go!")