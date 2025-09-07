list1 = [2, 5, 6]
list2 = [0, 3, 9]
sumResult = map(lambda x, y: x + y, list1, list2)
print(f"The sums of the lists are {list(sumResult)}")

def product(x, y):
    return x*y
number1 = [2, 7]
number2 = [9, 4]
productResult = list(map(product, number1, number2))
print(f"The products are {productResult}")

def sq(n):
    return n*n
numbers = [5, 3, 19]
result = list(map(sq, numbers))
print(f"The squares are {result}")