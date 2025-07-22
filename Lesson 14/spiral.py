import turtle

background = turtle.Screen()

background.bgcolor("light blue")
background.setup(300,400)
background.title("Spiral")
myPen = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        myPen.forward(size+1)
        myPen.left(45)
        size -= 5
    size += 1

