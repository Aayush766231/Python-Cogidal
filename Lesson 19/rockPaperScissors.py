import random
# 1 = rock, 2 = paper, 3 = scissors
print("Let's play rock, paper, scissors")
while True:
    computer = random.choice(["rock", "paper", "scissors"])
    player = input("What is your choice? ").lower()
    print("The computer chose", computer)
    if computer == "rock":
        if player == "rock":
            print("Tie. Try again!")
            continue
        if player == "paper":
            print("You win!")
            break
        if player == "scissors":
            print("You lost. Try again!")
            continue
    if computer == "paper":
        if player == "paper":
            print("Tie. Try again!")
            continue
        if player == "scissors":
            print("You win!")
            break
        if player == "rock":
            print("You lost. Try again!")
            continue
    if computer == "scissors":
        if player == "scissors":
            print("Tie. Try again!")
            continue
        if player == "rock":
            print("You win!")
            break
        if player == "paper":
            print("You lost. Try again!")
            continue