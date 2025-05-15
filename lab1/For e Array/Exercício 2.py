valores = []

while len(valores) < 10:
    valor = int(input(f"Digite o {len(valores)+1}º valor (distinto): "))
    if valor not in valores:
        valores.append(valor)
    else:
        print("Valor já digitado. Digite outro valor.")

maiores_que_100 = []

for num in valores:
    if num > 100:
        maiores_que_100.append(num)

print(f"Valores digitados: {valores}")
print(f"Quantidade de valores maiores que 100: {len(maiores_que_100)}")
print(f"Valores maiores que 100: {maiores_que_100}")
