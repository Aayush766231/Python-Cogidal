money = int(input("How much money will you give? "))
money100 = money//100
print(money100, "100 dollar notes")
x = (money%100)//50
print(x, "50 dollar notes.")
y = (money%50)//10
print(y, "10 dollar notes")

