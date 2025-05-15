valores = []

while len(valores) < 10:
    valor = int(input(f"Digite o {len(valores)+1}º valor (distinto): "))
    if valor not in valores:
        valores.append(valor)
    else:
        print("Valor já digitado. Digite outro valor.")

print("Valores pares e suas respectivas posições:")
for i in range(len(valores)):
    if valores[i] % 2 == 0:
        print(f"Posição {i} - Valor {valores[i]}")
