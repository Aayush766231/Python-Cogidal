import array as arr

a = arr.array('i', [1, 3, 5, 7, 3, 7, 9, 3])

print("The original integer array is:")
for i in range(len(a)):
    if i != len(a) - 1:
        print(a[i], end=", ")
    else:
        print(a[i])

print(f"The number 3 occurs {a.count(3)} times")

a.reverse()
a1 = arr.array('i', a)
print(f"The reverse of the array is {a1}")

