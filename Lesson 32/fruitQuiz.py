import random

class quiz:
    def __init__(self, question):
        self.question = question
    def questionCreation(self):
        print(f"What is a(n) {self.question}?")

fruit = {
    "Apple": "A red fruit",
    "Orange": "A round, sweet orange ball", 
    "Banana": "A yellow berry", 
    "Blueberry": "A small, blue ball"}
numberCorrect = 0
totalQ = 0

fruits = []
fruitAnswers = []
for i, j in fruit.items():
    fruits.append(i)
    fruitAnswers.append(j)

while True:
    #increases total questions asked by 1
    totalQ += 1
    #chooses a random key from the dictionary to be quizzed on
    number = random.randint(0, 3)
    questionNum = quiz(fruits[number])
    questionNum.questionCreation()
    #lists the possible answers
    print(f"1. {fruitAnswers[0]}")
    print(f"2. {fruitAnswers[1]}")
    print(f"3. {fruitAnswers[2]}")
    print(f"4. {fruitAnswers[3]}")
    answer = int(input())
    #checks answer
    if answer == number + 1:
        print("Correct!")
        numberCorrect += 1
    else:
        print(f"Incorrect. The actual answer was {fruitAnswers[number]}")
    #keep going?
    continuation = int(input('Enter a 1 to keep going, enter a 0 to end the quiz: '))
    if not continuation:
        break
print(f'You got {(numberCorrect/totalQ) * 100}% correct')