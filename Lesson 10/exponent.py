base = int(input("What is the original number? "))
exponent = int(input("What power do you want to raise it to? "))

for i in range(exponent + 1):
    if i == exponent:
        print(base**exponent, f"is {base} raised to the {exponent} power.")