import turtle

background = turtle.Screen()

background.bgcolor("black")
background.setup(300,400)
background.title("Spiral")
myPen = turtle.Turtle()
size = 0
penColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

while True:
    for i in range(len(penColors)):
        myPen.color(penColors[i])
        myPen.forward(size+1)
        myPen.left(45)
        size -= 5
    size += 1
    for i in range(len(penColors)):
        myPen.color(penColors[i])
        myPen.forward(size+1)
        myPen.left(45)
        size -= 5
    size += 1