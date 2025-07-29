vowel = "aeiou"

def character(string):
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] in vowel:
                print(string[i], "is a vowel")
            else:
                print(string[i], "is a consonant")

character(input("Enter sentence: "))