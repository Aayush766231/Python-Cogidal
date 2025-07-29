def fibonacci(x):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21
    if x == 1 or x == 0:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    
print(fibonacci(6))