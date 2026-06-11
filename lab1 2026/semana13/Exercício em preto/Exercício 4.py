colheitas = []
soma = 0

for i in range(5):
    valor = int(input("Digite a quantidade colhida: "))
    colheitas.append(valor)
    soma += valor

media = soma / 5

print("Soma:", soma)
print("Média:", media)
