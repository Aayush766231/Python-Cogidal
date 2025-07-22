import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
triangle1 = turtle.Turtle()
triangle2 = turtle.Turtle()

for i in range(3):
    triangle1.forward(70.0)
    triangle1.right(120)
triangle2.penup()
triangle2.goto(0, -35)
triangle2.pendown()
for i in range(3):
    triangle2.forward(70.0)
    triangle2.left(120)

turtle.done()