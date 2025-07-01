number1 = int(input("Enter two numbers: "))
number2 = int(input())

if number1 % number2 == 0:
    print(str(number1) + " is divisible by " + str(number2))
else:
    print(str(number1) + " is not divisible by " + str(number2))