#SET ZIP
s1 = {2, 6, 7, 9}
s2 = {'h', "p", 'k', 'n'}
s3 = set(zip(s1, s2))
print(s3)

#LIST ZIP
l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]

for x, y in zip(l1, l2[::-1]):
    print(x, y)

#ZIP TO DICTIONARY
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]
newDict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(newDict)

#MIX AND MATCH ZIP
l = [2, 5, 7]
s = {7, 8, 4}
for l, s in zip(l, s):
    print(l, s)

#UNEQUAL LENGTH ZIP
short = [9, 5, 7, 2]
long = [5, 7, 9, 2, 1, 10, 91]
newDict = {short: long for short, long in zip(short, long)} #cuts out the last 3 items in long
print(newDict)