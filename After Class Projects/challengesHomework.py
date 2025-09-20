import random

length = random.randint(10, 14)

def type():
    place = random.randint(1, 3)
    if place == 1:
        lowerLetter = "abcdefghijklmnopqrstuvwxyz"
        return random.choice(lowerLetter)
    elif place == 2:
        upperLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return random.choice(upperLetter)
    else:
        return random.randint(0, 9)
    
password = []
for i in range(length):
    password.append(type())

print("Your randomly generated password is:")
for i in password:
    print(i, end="")