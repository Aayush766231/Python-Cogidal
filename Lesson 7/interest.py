investment = float(input("How much did you invest? "))
rate = float(input("What was the rate? "))
time = int(input("For how long? "))

endCompound = investment*(1+(rate/100))**time
compoundInterest = endCompound - investment
print(round(endCompound, 2), round(compoundInterest, 2))

simpleInterest = (investment*rate*time)/100
print(simpleInterest)

