range1 = int(input("How many numbers are you multiplying? "))
print("Enter the numbers: ")
productNums = []
for i in range(range1):
    number = int(input())
    productNums.append(number)

tuple1 = tuple(productNums)
tupleAvg = (sum(tuple1))/len(tuple1)

print(f"The average of the numbers you entered was {tupleAvg}")
