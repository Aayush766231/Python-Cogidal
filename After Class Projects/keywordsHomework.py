def change(total, payment):
    if payment < total:
        return "Payment must be more than total"
    spareChange = payment - total
    return spareChange

print(f"{change(10, 12.5)} dollars is your change")