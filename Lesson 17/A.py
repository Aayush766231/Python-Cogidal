word = input("Enter a word here: ").upper()

for i in word:
    if i == "A":
        print(f"A is the {word.index("A") + 1}th letter")
        break
    if i == word[-1]:
        print(f"There is no a in {word}")
