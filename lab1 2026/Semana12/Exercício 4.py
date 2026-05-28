
def calcular_total(laranjas):
    if laranjas <= 12:
        total = laranjas * 0.40
    else:
        total = laranjas * 0.25

    return total

quantidade = int(input("Digite a quantidade de laranjas: "))

valor = calcular_total(quantidade)

print("Valor total: R$", valor)
