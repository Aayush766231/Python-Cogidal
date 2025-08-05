def change(total, payment):
    if payment < total:
        return "Payment must be more than total"
    spareChange = payment - total
    return spareChange

print(f"{change(float(input("How much did it cost? ")), float(input("How much did you pay? ")))} dollars is your change")