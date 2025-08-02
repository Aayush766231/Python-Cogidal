def digitsSum(number):
    if number == 0:
        return 0
    number = abs(number)
    return number % 10 + digitsSum(number // 10)

print(digitsSum(int(input("Enter number here: "))))