import math

class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print((self.radius)**2 * math.pi)
    def circumference(self):
        print(2*self.radius*math.pi)

rad = float(input("What is the radius of the circle? "))
ob = circle(rad)
ob.area()
ob.circumference()