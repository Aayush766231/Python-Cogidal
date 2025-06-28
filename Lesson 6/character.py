character = input("Enter a character here: ")

if character == character.upper():
    print(f"{character} is uppercase")
else:
    print(character, "is lowercase")

if character >= "A" and character <= "Z":
    print(f"{character} is uppercase")
else:
    print(character, "is lowercase")