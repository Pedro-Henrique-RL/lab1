kg_morango = float(input("Digite a quantidade (kg) de morango: "))
kg_maca = float(input("Digite a quantidade (kg) de maçã: "))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total = (kg_morango * preco_morango) + (kg_maca * preco_maca)

if kg_morango + kg_maca > 8 or total > 25:
    total *= 0.90  

print(f"Total a pagar: R$ {total:.2f}")
