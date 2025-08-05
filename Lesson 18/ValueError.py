try:
    number = int(input("Enter number: "))
    print(f"You gave {number}")
except ValueError:
    print("Exception: the value you entered is not a number")
finally:
    print("Enter a number please")