def add(P, Q):
    sum = P + Q
    return sum
def subtract(P, Q):
    difference = P - Q
    return difference
def mult(P, Q):
    product = P * Q
    return product
def div(P, Q):
    quotient = P / Q
    return quotient

print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
operation = input("Choose your operation (a/b/c/d): ").lower()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "a":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == "b":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == "c":
    print(f"{num1} * {num2} = {mult(num1, num2)}")
elif operation == "d":
    print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("Invalid input")