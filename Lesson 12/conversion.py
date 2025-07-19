number = int(input("Enter number here: "))
numberBinary = ""


while number > 0:
    remainder = 0
    remainder = str(number % 2)
    numberBinary = remainder + numberBinary
    number //= 2

print(numberBinary)