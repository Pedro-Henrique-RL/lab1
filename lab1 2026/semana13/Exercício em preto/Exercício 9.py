import random

ids = []

for i in range(10):
    ids.append(random.randint(1, 100))

print("IDs pares:")

for numero in ids:
    if numero % 2 == 0:
        print(numero)
