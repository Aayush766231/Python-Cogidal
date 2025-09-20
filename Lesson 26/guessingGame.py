import random
import time

number = random.randint(1, 100)

def intro():
    print("What's your name?")
    global name 
    name = input()
    print(f"{name}, we're going to play a game. I'm thinking of a number between 1 and 100")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0

    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            #TIME TO CHECK INPUT - MUST FIRST MAKE IT AN INTEGER
            guess = int(enter)
            if guess >= 1 and guess <= 100:
                guessesTaken += 1
                if guessesTaken < 6:
                    if guess < number:
                        print("Too low!")
                    if guess > number:
                        print("Too high!")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again")
                    if guess == number:
                        break
            if guess < 1 or guess > 100:
                time.sleep(.25)
                print("Silly! That's not in the range")
                print("Please enter a number between 1 and 100 this time!")
        except:
            print(f"{enter} is not a number. Please try again")
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job {}! You guessed it in {} tries!".format(name, guessesTaken))
    if guess != number:
        print("Sorry, I was thinking of {}".format(number))

playAgain = "Y"
while playAgain == "Y" or playAgain == "y" or playAgain == "Yes":
    intro()
    pick()
    print("Again?")
    playAgain = input()