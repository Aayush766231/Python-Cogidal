myChar = input("Enter character here: ")

if myChar >= "a" and myChar <= "z":
    print(f"{myChar} is a lowercase letter")
elif myChar >= "A" and myChar <= "Z":
    print(myChar, "is an uppercase letter")
elif myChar.isdigit():
    print(f"{myChar} is a number")
else:
    print(myChar, "is a special character")