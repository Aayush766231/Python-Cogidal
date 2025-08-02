upperBound = int(input("What number do you want prime numbers too? "))

print(2, end= ", ")
print(3, end= ", ")
print(5, end= ", ")
print(7, end= ", ")
for i in range(2,upperBound):
    if i % 2 == 0:
        pass
    elif i % 5 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 7 == 0:
        pass
    else:
        print(i, end= ", ")
print("These are prime numbers up to 30")