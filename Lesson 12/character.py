word = input("Enter a word here: ").upper()
#char = input("What character do you want to count? ").upper()


for i in range(len(word)):
    count = 0
    j = word[i].upper()
    for x in range(len(word)):
        if word[x] == j:
            count += 1
    print(f"{j} comes up {count} times")    
#print(f"{char} comes up {count} times in {word}")