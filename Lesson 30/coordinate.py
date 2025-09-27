class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return ("({0}, {1})".format(self.x, self.y))
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(2, 3)
p2 = Point(4, 6)
p3 = Point(2, 3)
print(p1)
print(p1 + p2)
print(p1 - p2)
print(p1 == p3)

class list:
    def __init__(self, x = [0], y = [2]):
        self.x = x
        self.y = y
    def __len__(self):
        return len(self.y)

a = [2, 5, 6, 2]
b = [9, 4, 2]
l1 = list(a, b)
print(len(l1))