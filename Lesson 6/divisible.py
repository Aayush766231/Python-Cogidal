number = int(input("Enter number: "))

if number%3 == 0 and number%5 == 0:
    print(f"{number} is divisible by 3 and 5")
elif number%3 == 0 and number%5 != 0:
    print(f"{number} is divisible by 3 but not by 5")
elif number%3 != 0 and number%5 == 0:
    print(number, "is divisible by 5 but not 3")
else:
    print(number, "is not divisible by 3 or 5")
#activitiy 2
number1 = int(input("Enter three numbers: "))
number2 = int(input())
number3 = int(input())

if number1 > number2 and number1 > number3:
    print(f"{number1} is the largest number")
elif number2 > number1 and number2 > number3:
    print(number2, "is the largest number")
else:
    print(f"{number3} is the largest number")