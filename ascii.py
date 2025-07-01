letter = input("Enter letter here: ")
print(ord(letter))

letters = input("Enter letters here: ")
letters1 = input()
letters2 = input()
i = 0
lettersArray = [letters, letters1, letters2]

while i < len(lettersArray): 
    print(ord(lettersArray[i]))
    i+=1
