class vehicle:
    def __init__(self, distance):
        self.distance = distance
    def fare(self):
        return self.distance * 10
class bus(vehicle):
    def __init__(self, distance):
        super().__init__(distance)
far = int(input("How many km are you traveling? "))
ride = bus(far)
print("You have to pay", ride.fare())