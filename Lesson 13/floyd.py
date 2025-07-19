rows = int(input("Enter number of rows: "))
initialNumber = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(initialNumber, end= " ")
        initialNumber += 1
    print()