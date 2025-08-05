try:
    number = int(input("Enter a number: "))
    while True:
        print("bye")
        if number % 2 == 0:
            while True:
                print("bye")
        elif number % 2 == 1:
            break
        else:
            raise ValueError
except ValueError as ex:
    print("Exception:", ex, "is not a number")
        