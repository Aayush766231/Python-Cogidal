newList = []
listOfWords = []

length = int(input("How long is the list going to be? "))

print("Enter your words: ")
for i in range(length):
    words = input()
    listOfWords.append(words)

def letterMatch(wordList):
    for i in wordList:
        letter1 = i[0]
        letterEnd = i[-1]
        if letter1.upper() == letterEnd.upper():
            newList.append(i)
    return newList

print(letterMatch(listOfWords), "have matching first and last letters, of the words you entered.")