class person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)
class employee(person):
    def __init__(self, name, id, salary, post):
        super().__init__(name, id)
        self.salary = salary
        self.post = post
# creation of a new employee
a = employee("Aayush", 2009, 30000, "Intern")
# displaying name and id
a.display()