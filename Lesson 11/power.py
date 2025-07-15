number = int(input("What is the base number? "))
power = int(input("What is the exponent? "))
i = 1

while i <= power:
    print(f"{number} to the {i} power is", number**i)
    i+=1