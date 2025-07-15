lower = int(input("What is your lower range? "))
upper = int(input("What is your upper range? "))


for i in range(lower, upper + 1):
    truth = True
    if i > 1:
        for x in range(2,i):
            if i % x == 0:
                truth = False
                break
        if truth == True:
            print(i)
        