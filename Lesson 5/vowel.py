letter = input("Insert letter: ").lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter =="u":
    print(f"{letter} is a vowel")
else:
    print(letter, "is a consonant")