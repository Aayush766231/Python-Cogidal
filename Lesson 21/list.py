L = [1, 10, 3, 8, 7, 4, 9, 11, 5]

sum = 0
for i in L:
    sum += i
print(sum)

avg = sum/len(L)
print(avg)

L.sort()
print(L)
print(f"The max is {max(L)}")
print(f"The minimum is {min(L)}")

L.sort(reverse= True)
print(L)

strings = ["hi", "hello", "bye", "education"]
longString = sorted(strings)
print(longString)
shortString = sorted(strings, reverse= True)
print(shortString)