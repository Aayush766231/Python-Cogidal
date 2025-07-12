sentence = input("Enter sentence here: ").strip()
wordCounter = 1
spaces = 0
for i in range(len(sentence)):
    if sentence[i] == " ":    
        spaces += 1
        wordCounter = spaces + 1
        

print(wordCounter, "words in the sentence")