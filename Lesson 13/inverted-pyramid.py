rows = int(input("Enter number of rows: "))

space = 0

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i, f", {i}")

    


#if rows % 2 == 0:
#    halfDiamond = int(rows/2)
#else:
#    halfDiamond = int((rows/2)) + 1

#space = halfDiamond - 1

#for i in range(1, halfDiamond + 1):
#    for j in range(1, space + 1):
#        print(end= "  ")
#    space -= 1
#    num = 1
#    for j in range(2*i - 1):
#        print(end= str(num) + " ")
#        num += 1
#    print()
