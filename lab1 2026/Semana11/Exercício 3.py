numeros = []

print("Digite 10 valores inteiros distintos:\n")

while len(numeros) < 10:
    num = int(input(f"Digite o {len(numeros)+1}º valor: "))
    if num in numeros:
        print("Valor repetido! Digite um valor diferente.")
    else:
        numeros.append(num)

print("\nValores pares e suas posições:")
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(f"Posição {i+1} -> valor {numeros[i]}")
