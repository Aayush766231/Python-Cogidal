from abc import ABC, abstractmethod

class car:
    def __init__(self, owner):
        self.owner = owner
    @abstractmethod
    def model(self):
        pass
    @abstractmethod
    def fuelType(self):
        pass
    @abstractmethod
    def maxSpeed(self):
        pass
class Ferrari(car):
    def __init__(self, owner):
        super().__init__(owner)
    def model(self):
        print("This is a Ferrari")
    def fuelType(self):
        print("It runs on gas")
    def maxSpeed(self):
        print("Max Speed: 300")
class BMW(car):
    def __init__(self, owner):
        super().__init__(owner)
    def model(self):
        print("This is a BMW")
    def fuelType(self):
        print("It runs on gas")
    def maxSpeed(self):
        print("Max Speed: 200")
a = Ferrari("Jill")
b = BMW("Jack")

for make in (a, b):
    print(make.owner)
    make.model()
    make.fuelType()
    make.maxSpeed()