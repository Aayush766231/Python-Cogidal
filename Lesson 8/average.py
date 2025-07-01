a = int(input("Enter three numbers: "))
b = int(input())
c = int(input())
avg = (a + b + c)/3
print(f"The average is {avg}")

if avg > a and avg > b:
    print(f"{avg} is bigger than {a} and {b}, but not {c}")
elif avg > a and avg > c:
    print(f"{avg} is bigger than {a} and {c}, but not {b}")
elif avg > c and avg > b:
    print(f"{avg} is bigger than {c} and {b}, but not {a}")
elif avg > a:
    print(f"{avg} is only bigger than {a}")
elif avg > b:
    print(f"{avg} is only bigger than {b}")
elif avg > c:
    print(f"{avg} is only bigger than {c}")
else:
    print("Invalid input")