# EXERCÍCIO 3

litros = float(input("Quantidade de litros: "))
valor = float(input("Valor total: "))

if litros >= 20 and valor > 100:
    desconto = valor * 0.10
elif litros >= 20 and valor <= 100:
    desconto = valor * 0.05
else:
    desconto = 0

valor_final = valor - desconto

print("Desconto:", desconto)
print("Valor final:", valor_final)
