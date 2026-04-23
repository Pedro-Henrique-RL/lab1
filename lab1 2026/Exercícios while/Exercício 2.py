codigo = -1
contador = 0

while codigo != 0:
    codigo = int(input("Digite o código (0 para parar): "))
    if codigo == 1040:
        contador += 1

print("Código 1040 foi digitado", contador, "vezes.")
