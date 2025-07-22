import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(400,500)
polygon = turtle.Turtle()

numSides = int(input("How many sides do you want? "))
angle = 360/numSides
sideLength = 70

for i in range(numSides):
    polygon.forward(sideLength)
    polygon.right(angle)

turtle.done()