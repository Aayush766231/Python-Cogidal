import time

class Employee():
    def __init__(self):
        print("Employee created")
    
    def __del__(self):
        print("Destructor Called")

def objCreation():
    print("Making object...")
    global obj
    obj = Employee()
    print("Deleting object")
    return obj

print("EMPLOYEE CREATION")
time.sleep(.5)
objCreation()
time.sleep(.5)
print("TERMINATED")
time.sleep(.5)
del obj