range1 = int(input("How many numbers are you multiplying? "))
print("Enter the numbers: ")
productNums = []
for i in range(range1):
    number = int(input())
    productNums.append(number)

originalTuple = tuple(productNums)
product = 1

for i in originalTuple:
    product *= i
print(product)