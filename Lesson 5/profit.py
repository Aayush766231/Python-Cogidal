buyingPrice = float(input("How much did you buy it for? "))
sellingPrice = float(input("How much are you selling for? "))

if sellingPrice > buyingPrice:
    profit = sellingPrice - buyingPrice
    print("You have a profit of", profit)
else:
    loss = buyingPrice - sellingPrice
    print(f"You are losing {loss} dollars")