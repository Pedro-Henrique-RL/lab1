import random

ids = []

for i in range(10):
    ids.append(random.randint(1, 50))

pares = 0
impares = 0

for numero in ids:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Array:", ids)
print("Pares:", pares)
print("Ímpares:", impares)
