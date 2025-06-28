x = 4
if type(x) is int:
    print(x, "is an integer")

a = 9.0
if type(a) is float:
    print(f"{a} is a decimal")

x = 24
y = 24

if x is y:
    print("x and y have the same value")
y = 30
if x is not y:
    print("x and y have different values")

list1 = [2,4,6,8]
list2 = [2,4,6,8]
if list1 is list2:
    print("both lists are the same")