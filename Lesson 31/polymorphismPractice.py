from abc import ABC, abstractmethod

class job(ABC):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def salary(self):
        print("{}'s salary is {} per week".format(self.name, 10*self.value))
    @abstractmethod
    def role(self):
        pass
class manager(job):
    def __init__(self, name, value):
        super().__init__(name, value)
    def role(self):
        print("{} make sure everything runs smoothly and people are working hard".format(self.name))
class employee(job):
    def __init__(self, name, value):
        super().__init__(name, value)
    def role(self):
        print(f"{self.name} does the labor that the job calls for")

Bob = manager("Billy", 100)
Jack = employee("Jonathan", 10)

for person in (Bob, Jack):
    person.salary()
    person.role()