print("Welcome to the restaurant! Our menu is: ")
print("1. Pizza")
print("2. Burgers")
print("3. Traditional")
print("4. Pasta")
order = int(input("What will your order be?"))

if order == 1:
    type = input("What kind of pizza (S, M, L)? ").upper()

    if type == "S":
        print("We will be getting your small pizza out soon.")
    elif type == "M":
        print("Your medium pizza will be out soon.")
    else:
        print("Your large pizza is coming")
elif order == 2:
    burgerType = input("Do you want a veg (1) or a nonveg (2)? ")

    if burgerType == 1:
        print("We will be getting your veg burger")
    else:
        print("Your burger is coming soon")
elif order == 3:
    print("1. Butter Naan")
    print("2. Garlic Naan")
    bread = int(input("What type of naan do you want?"))

    if bread == 1:
        print("Ok, that's butter naan")
    else:
        print("We'll have your garlic naan ready soon.")
    
    print("1. Paneer")
    print("2. Dal")
    dish = int(input("What side dish will accompany it?"))

    if dish == 1:
        print("Your paneer will be coming soon")
    else:
        print("Enjoy your dal")
else:
    print("1. Alfredo")
    print("2. 4 Cheese")
    pastaType = int(input("What kind of pasta? "))

    if pastaType == 1:
        print("Alfreda pasta is a good choice")
    else:
        print("Four cheese is very good")

print("We'll have your order out soon. ")