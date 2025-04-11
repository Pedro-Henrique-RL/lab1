contador = 0
numero = int(input("Digite um numero (numero 0 para parar): "))

while numero != 0:
    if numero == 10:
        numero = int(input("Digite um numero (numero 0 para parar): "))
        contador += 1
print("O numero 10 apareceu", contador, "vezes")
