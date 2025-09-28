from abc import ABC, abstractmethod

class ABSclass(ABC):
    def print(self, x):
        print("Passed value:", x)
    @abstractmethod
    def task(self):
        print("We are inside ABSclass right now")
class testClass(ABSclass):
    def task(self):
        print("We are inside a testClass")

obj1 = testClass()
obj1.task()
obj1.print(4)