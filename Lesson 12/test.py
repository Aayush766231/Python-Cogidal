num = 7
truth = True

for i in range(2, num):
    if num % i == 0:
        truth = False
        break
if truth == True:
    print(num)