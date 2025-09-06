#Activity 1
set1 = {1, 2, 3, 4, 5}
print(set1)

set1 = {1, 2, "hello", (1, 2)}
print(set1)

set1 = set([1, 2, 4, 5, 6, 3])
print(set1)

set2 = {0}
for i in set1:
    set2.add(i)
print(set2)

set1.update([6, 3, 8, 9])
print(set1)

numSet = {0, 5, 2, 7, 1, 9}
print(numSet, "is the original")
numSet.pop()
print(numSet)
numSet.remove(9)
print(numSet)
numSet.clear()
print(numSet)

# Activity 2
newSet = {5, 0, 4, 7, 2, 9}
oldSet = {3, 5, 0, 1, 6, 8}

print(newSet)
print(oldSet)

print("Union:")
print(newSet.union(oldSet))

print("Intersection:")
print(newSet.intersection(oldSet))

print("Difference (oldSet):")
print(oldSet.difference(newSet))

print("Differnce (newSet):")
print(newSet.difference(oldSet))

print("Symmetric Difference:")
print(newSet.symmetric_difference(oldSet))