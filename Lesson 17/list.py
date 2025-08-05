list = []
#boundary = int(input("How many words do you want to sort? "))
letter = input("What letter are we filtering out? ").lower()
condition = True

while condition:
    question = input("Continue? Y or N: ")
    if question.upper() == "Y":
        list.append(input("Enter a word: "))
    else:
        break
newList = []
for i in list:
    if letter in i.lower():
        continue
    else:
        newList.append(i)
print(newList)
