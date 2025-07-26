def greeting(status = "tired"):
    print("Hello")
    if status.lower() == "good":
        print("That's nice to hear")
    else:
        print("Oh no")

greeting()