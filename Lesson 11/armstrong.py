number = int(input("Enter a number: "))
numberCopy = number
i = 0
newNumber = 0

while numberCopy > 0:
    digit = numberCopy % 10
    newNumber += digit ** 3
    numberCopy //= 10

if newNumber == number:
    print(f"{number} is an Armstrong number")
else:
    print(number, "is not an Armstrong number")