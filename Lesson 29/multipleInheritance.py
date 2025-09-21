class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoIsThis(self):
        print("Bird")
    def swim(self):
        print("Swim Faster")
class landAnimal:
    def __init__(self):
        print("Exists on land")
    def who(self):
        print("Land Animal")
    def run(self):
        print("Run faster")
class Penguin(Bird, landAnimal):
    def __init__(self):
        landAnimal.__init__(self)
        Bird.__init__(self)
        print("Penguin is ready")

a = Penguin()
a.run()
a.whoIsThis()
print(issubclass(Penguin, (Bird, landAnimal)))

