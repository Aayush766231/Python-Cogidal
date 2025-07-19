number = int(input("Enter number here: "))
numberCopy = number
digitsNumber = 0

while numberCopy > 0:
    numberCopy //= 10
    digitsNumber += 1

print(f"There are {digitsNumber} digits in {number}")