keywords = []
values = []
length = int(input("How long is your dictionary going to be? "))
print("Enter your keywords first: ")
for i in range(length):
    keyword = input()
    keywords.append(keyword)
print("Now your values: ")
for i in range(length):
    value = input()
    values.append(value)

originalDict = {}
for i in range(len(values)):
    originalDict[keywords[i]] = values[i]
print(originalDict)