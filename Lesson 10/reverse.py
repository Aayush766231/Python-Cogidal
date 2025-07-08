sentence = input("Enter a sentence: ")
reverseSentence = ""
for i in range(len(sentence) - 1, -1, -1):
    reverseSentence = reverseSentence + sentence[i] 

print(reverseSentence)