number = int(input("Enter a number here: "))
numberCopy = number
strongNumber = 0


while numberCopy > 0:
    digit = numberCopy % 10
    digitFactorial = 1
    while 1 <= digit:
        digitFactorial *= digit
        digit -= 1
    strongNumber = strongNumber + digitFactorial
    numberCopy //= 10

if strongNumber == number:
    print(f"{number} is a strong number")
else:
    print(f"{number} isn't strong.")