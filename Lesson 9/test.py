medical = input("Do you have a medical cause (Y or N)? ")
attendence = int(input("What is your attendance? "))

if medical.upper() == "Y":
    print("You are allowed to take the exam.")
else:
    if attendence >= 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed.")