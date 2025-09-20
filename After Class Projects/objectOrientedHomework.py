class pet:
    species = 'dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

shiba = pet("Shiba Inu", "orange")
lab = pet("Labrador", "golden")

print(f"Both Shiba and Lab are {shiba.species}s")
print(f"Shiba is a {shiba.breed} with {shiba.color} fur")
print("However, Lab is a {} with {} colored fur".format(lab.breed, lab.color))