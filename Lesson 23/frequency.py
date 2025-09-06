originalDict = {}
length = int(input("How many things are you checking? "))
print("Enter the name and its corresponding number separately:")
for i in range(length):
    keyVal = input()
    valueVal = int(input())
    originalDict[keyVal] = valueVal

valueNum = int(input("What number are you checking for? "))
newDict = {"placeholder": valueNum}


for key,value in originalDict.items():
    if value in newDict.values():
        newDict[key] = value

if len(newDict) - 1 == 1:
    print(f"{valueNum} appears {len(newDict) - 1} time")
else:
    print(f"{valueNum} appears {len(newDict) - 1} times")