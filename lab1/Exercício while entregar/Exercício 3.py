numero = -1
cont10 = 0

while numero != 0:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 10:
        cont10 += 1

print("O número 10 foi digitado", cont10, "vezes.")
