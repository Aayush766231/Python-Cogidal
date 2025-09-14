class parrot:
    # class variable for all parrots
    species = 'bird'
    
    #instance vars individualized
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is younger, at {} years old".format(blu.name, blu.age))
print("{} is older, being {} years old".format(woo.name, woo.age))