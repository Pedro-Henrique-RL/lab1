valores = []

print("Digite 10 valores inteiros distintos:\n")

while len(valores) < 10:
    num = int(input(f"Digite o {len(valores)+1}º valor: "))
    if num in valores:
        print("Valor repetido! Digite um valor diferente.")
    else:
        valores.append(num)

maiores_100 = []
for num in valores:
    if num > 100:
        maiores_100.append(num)

print("\nValores digitados:", valores)
print(f"Quantidade de valores maiores que 100: {len(maiores_100)}")
print("Valores maiores que 100:", maiores_100)
