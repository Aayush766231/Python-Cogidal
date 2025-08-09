try:
    age = int(input("Enter an age: "))
    if age % 2 != 0:
        raise TypeError
    else:
        print("Age accepted")
except ValueError as ex:
    print(f"Exception: {ex}, is not a number")
except TypeError:
    print("Age is not valid")
finally:
    print("Try again?")
