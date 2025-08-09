import random

playing = True
number = random.randint(10, 20)

print("The guessing game is a game where you have to guess the value of the hidden number. Let's begin.")
while playing:
    guess = int(input("Enter a number less than 100: "))
    if guess == number:
        print("Amazing! You guessed the number")
        print("The number was", number)
        break
    else:
        print("Try again!")