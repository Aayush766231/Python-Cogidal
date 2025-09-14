class vehicle:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

requestedMileage = int(input("How far do you want it to go per gallon? "))
modelX = vehicle(240, requestedMileage)

print(f"The max speed of the Model X is {modelX.maxSpeed}.")
print(f"The mileage of it will be {modelX.mileage}.")