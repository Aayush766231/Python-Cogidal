def factorial(x):
    '''A recursive function that takes a number and finds its factorial.'''

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial.__doc__)
print("The factorial of 5 is", factorial(5))