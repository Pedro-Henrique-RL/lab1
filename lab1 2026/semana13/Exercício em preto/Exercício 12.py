kg_colhidos = []
preco_por_kg = []
valor_por_arvore = []

for i in range(5):
    kg = float(input("Kg colhidos: "))
    kg_colhidos.append(kg)

for i in range(5):
    preco = float(input("Preço por kg: "))
    preco_por_kg.append(preco)

for i in range(5):
    valor = kg_colhidos[i] * preco_por_kg[i]
    valor_por_arvore.append(valor)

print("Valores por árvore:")
print(valor_por_arvore)
