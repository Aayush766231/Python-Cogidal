rows = int(input("Enter number of rows: "))

if rows % 2 == 0:
    halfDiamond = int(rows/2)
else:
    halfDiamond = int((rows/2)) + 1

space = halfDiamond - 1

for i in range(1, halfDiamond + 1):
    for j in range(1, space + 1):
        print(end= " ")
    space -= 1
    num = 1
    for j in range(2*i - 1):
        print(end= str(num))
        num += 1
    print()
space = 1
for i in range(1, halfDiamond):
    for j in range(1, space + 1):
        print(end= " ")
    space += 1
    num = 1
    for j in range(1, 2*(halfDiamond - i)):
        print(end= str(num))
        num += 1
    print()