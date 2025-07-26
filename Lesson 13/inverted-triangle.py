rows = int(input("How many rows? "))
spaces = 4

for i in range(1, rows + 1):
    for j in range(1):
        print(" " * spaces, end= "")
    spaces -= 1    
    for j in range(i):
        print("*", end="")
    print()