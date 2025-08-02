

num = int(input("What number are you starting from? ")) - 1
odd = 0
numList = []
while odd < 3:
    num += 1
    if num % 2 == 0:
        continue
    else:
        odd += 1
        numList.append(num)
print(numList)