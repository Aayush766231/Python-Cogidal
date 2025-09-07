#LIST COMPREHENSION
newList = [x**3 for x in range(10) if x%2 == 1]
print(newList)

#NESTED LIST COMPREHENSION
newList = [x*y for x in range(1, 10) for y in range(1, 10) if x*y not in newList]
print(newList)

#TABLE
table = [[i * j for i in range(10)] for j in range(5)]
print(table)

#3D TABLE
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
depth = int(input("How deep? "))
table3D = [[[x for x in range(columns)] for x in range(rows)] for x in range(depth)]
print(table3D)