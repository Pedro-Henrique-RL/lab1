
def somar_fazendas(lista1, lista2):
    soma = []

    for i in range(len(lista1)):
        total = lista1[i] + lista2[i]
        soma.append(total)

    return soma

fazenda_a = []
fazenda_b = []

print("Produção da Fazenda A")
i = 0
while i < 5:
    valor = int(input(f"Digite a produção do lote {i+1}: "))
    fazenda_a.append(valor)
    i += 1

print("\nProdução da Fazenda B")
i = 0
while i < 5:
    valor = int(input(f"Digite a produção do lote {i+1}: "))
    fazenda_b.append(valor)
    i += 1

resultado = somar_fazendas(fazenda_a, fazenda_b)

print("\nProdução Fazenda A:", fazenda_a)
print("Produção Fazenda B:", fazenda_b)
print("Soma das produções:", resultado)
