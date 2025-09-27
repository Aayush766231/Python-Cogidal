class grandparent:
    def __init__(self, name, temperament):
        self.name = name
        self.temperament = temperament
    def display(self):
        print(self.name)
        print(self.temperament)
class parent(grandparent):
    def __init__(self, name, temperament, generation):
        super().__init__(name, temperament)
        self.generation = generation
    def type(self):
        print("We are rich")
class child(parent):
    def __init__(self, name, temperament, generation, gender):
        super().__init__(name, temperament, generation)
        self.gender = gender
#Creation of object in grandchild
a = child("Aayush", "Happy", "Z", "Male")
a.display()
a.type()
print(a.generation)
print(a.gender)