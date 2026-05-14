
dentro = 0
fora = 0

for i in range(10):

    numero = int(input("Digite um número: "))

    if numero >= 10 and numero <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print("Dentro do intervalo:", dentro)
print("Fora do intervalo:", fora)
