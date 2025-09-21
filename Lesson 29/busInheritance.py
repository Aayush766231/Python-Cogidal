class vehicle:
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage
class bus(vehicle):
    pass
schoolBus = bus("School Volvo", 180, 12)
print(f"The school bus is a {schoolBus.name} and has a max speed of {schoolBus.maxSpeed}, with a mileage of {schoolBus.mileage}")