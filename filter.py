from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

filper al igualque map toma los mismos argumentos, pero ahora puedes hacer un condicionante y solo devuelve
los que seantrue
