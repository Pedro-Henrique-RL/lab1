import random

equipe = []
pragas = []

for i in range(5):
    valor = float(input("Força da equipe: "))
    equipe.append(valor)

while len(pragas) < 5:
    numero = random.randint(1, 100)

    if numero not in pragas:
        pragas.append(numero)

protegidos = 0
perdidos = 0

print("\nResultados:")

for i in range(5):
    print("Lote", i)

    if equipe[i] > pragas[i]:
        print("Protegido")
        protegidos += 1
    else:
        print("Praga resistiu")
        perdidos += 1

print("\nForças da equipe:", equipe)
print("Forças das pragas:", pragas)

print("Lotes protegidos:", protegidos)
print("Lotes perdidos:", perdidos)
