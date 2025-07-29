def cube(number):
    number = number**3
    return number

def byThree(number):
    if number % 3 == 0:
        return cube(number)
    else:
        print("The number is not divisible by three")

print(byThree(int(input("Enter a number: "))))