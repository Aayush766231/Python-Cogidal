try:
    num1 = int(input("Enter two numbers: "))
    num2 = int(input())
    print(num1 / num2)

    string = "hello"
    index = int(input("What index value do you want to access? "))
    print(string[index])

    add1 = int(input("enter a number: "))
    add2 = input("Enter another: ")

    addTotal = add1 + add2
    print(addTotal)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError as ex:
    print(ex, ", in other words, that's not a number")
except IndexError:
    print(f"there is no value at index {index} in string")
except TypeError:
    print("you cannot add a string and an integer - issue with code")
except:
    print("report code")
finally:
    print("run program again")
