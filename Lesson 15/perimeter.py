import math

def perimeter(shape):
    if shape.lower() == "rectangle":
        length = int(input("What is the length? "))
        width = int(input("What is the width? "))
        return 2*(length + width)
    if shape.lower() == "square":
        sideLength = int(input("What is the length of one side? "))
        return 4*sideLength
    if shape.lower() == "circle":
        radius = int(input("What is the radius? "))
        return math.pi*2*radius
    
print(perimeter(input("What shape? ")))