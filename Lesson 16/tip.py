global bill
bill = float(input("How much did you spend on the bill? "))

def totalBill(tipPercent):
    newBill = bill * (1 + tipPercent)
    return newBill

taxedBill = totalBill(float(input("How much will you tip? ")))

print(taxedBill)