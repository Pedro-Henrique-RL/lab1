# EXERCÍCIO 5

morango = float(input("Kg de morango: "))
maca = float(input("Kg de maçã: "))

if morango <= 5:
    preco_morango = morango * 2.5
else:
    preco_morango = morango * 2.2

if maca <= 5:
    preco_maca = maca * 1.8
else:
    preco_maca = maca * 1.5

total = preco_morango + preco_maca

if morango + maca > 8 or total > 25:
    desconto = total * 0.10
else:
    desconto = 0

total_final = total - desconto

print("Total a pagar:", total_final)
