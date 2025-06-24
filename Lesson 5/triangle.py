side1 = int(input("Insert the length of the sides of a triangle: "))
side2 = int(input())
side3 = int(input())

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("It's a triangle")
else:
    print("It's not a triangle")