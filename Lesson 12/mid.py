number = int(input("Enter a number: "))
numberCopy = number
mult = 1
digitsNumber = 0

while numberCopy > 0:
    numberCopy //= 10
    digitsNumber += 1
if digitsNumber > 2:
    number //= 10
    for x in range(digitsNumber - 2):
        mult = mult * (number % 10)
        number //= 10
    print(mult)