balance = float(input("What is your balance in the bank? "))
pin = int(input("Enter 4-digit pin: "))

correctPin = 1896

if pin == correctPin:
    withdrawal = int(input("How much will you withdraw? "))
    if withdrawal > 0:
        if withdrawal > balance:
            print("Invalid withdrawal amount")
        else:
            print(f"You have withdrawan ${withdrawal}")
            balance = balance - withdrawal
            print(f"Your new balance is ${balance}")
    else:
        print("Invalid withdrawal amount")
else:
    print("Incorrect pin")