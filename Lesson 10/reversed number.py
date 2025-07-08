upper = int(input("What is the biggest number you want? "))

for i in range(upper, 0, -1):
    print(i, end= ", ")
    if i == 1:
        print("0")

