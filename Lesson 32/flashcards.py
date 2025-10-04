class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return "{}: {}".format(self.word, self.meaning)

flash = []
print("Welcome to FastFlash, where you can make flashcards as soon as possible in order to help you prepare for an exam.")
while True:
    #Takes the word and its meaning from user
    word = input("Enter a word: ")
    definition = input("What is it's definition? ")
    #inserts that set into flash
    flash.append(flashcard(word, definition))
    #asks for another one or if to end
    option = int(input("Enter 1 to keep going, enter 0 to signify that you have all the flashcards needed: "))
    if not option:
        break
    else:
        print("1 more!")
#creates a break line to separate the program from the flashcards
print("\nFlashcards created:")
for i in flash:
    print(i)