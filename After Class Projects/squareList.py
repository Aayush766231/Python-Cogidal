minRange = int(input("Enter the smallest number to be squared: "))
maxRange = int(input("Enter the biggest number: "))
listSquared = []

while minRange < maxRange + 1:
    number = minRange ** 2
    listSquared.append(number)
    minRange += 1

evenList = []
oddList = []
for i in listSquared:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print(f"The even squares are {evenList}")
print(f"The odd squares are {oddList}")