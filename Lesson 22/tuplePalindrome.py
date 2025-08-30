def palind(r):
    newTuple = r[::-1]
    if newTuple == r:
        return "The numbers form a palindrome"
    else:
        return "That's not a palindrome"

range1 = int(input("How many numbers? "))
print("Enter your numbers: ")
list = []
for i in range(range1):
    number = int(input())
    list.append(number)
tuple1 = tuple(list)

print(palind(tuple1))