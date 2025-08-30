tuplex = (True, "False", 3.2, 19)
print(tuplex)

tupley = (10, 4, 3, 2, 19, 27, 7)
print(tupley)
tupley += (9,)
print(tupley)

tuple50 = (50, 65, 2, 50, 39, 50)
print(tuple50.count(50))

tuple1 = (2, 4, 20, 45, 24, "Hello", "bye", help)
sliced = tuple1[3:5]
print(sliced)
sliced = tuple1[:6]
print(sliced)

tupleMult = (3, 5, 10)
tupleMult *= 3
print(tupleMult)

tupleTotal = (2, 5, 20, 1)
print(min(tupleTotal))
print(max(tupleTotal))
print(sum(tupleTotal))