print("1. Bike")
print("2. Car")
choice = int(input("What vehicle do you want? "))

if choice == 1:
    print("1. Scooter")
    print("2. Motorbike")
    choice2 = int(input("What type of bike do you want? "))

    if choice2 == 1:
        print("You chose a scooter")
    else:
        print("You chose a motorbike")
elif choice == 2:
    print("1. Sedan")
    print("2. SUV")
    print("3. Minivan")
    choice3 = int(input("What kind of car do you want? "))

    if choice3 == 1:
        print("You chose a sedan")
    elif choice3 == 2:
        print("You chose an SUV")
    else:
        print("You chose a minivan")
else:
    print("Wrong choice!")