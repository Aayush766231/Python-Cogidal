def shutdown(condition):
    '''If a certain condition is met, this will end the program, resulting in you needing to start it up again'''
    print(shutdown.__doc__)
    if condition.upper() == "Y":
        end = "Program ended"
        return print(end)
    else:
        shutdown(input("End the program? "))

print(shutdown(input("End the program? ")))