
def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    return media

producao = []

i = 0
while i < 8:
    valor = float(input(f"Digite a produção de azeitonas do dia {i+1} em kg: "))
    producao.append(valor)
    i += 1

media = calcular_media(producao)
print(f"\nA média de produção é: {media:.2f} kg")

print("Produções acima da média:")
for valor in producao:
    if valor > media:
        print(f"{valor} kg")
