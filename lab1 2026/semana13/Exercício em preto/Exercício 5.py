producao = []

for i in range(5):
    valor = int(input("Digite a produção da árvore: "))
    producao.append(valor)

maior = producao[0]
menor = producao[0]

indice_maior = 0
indice_menor = 0

for i in range(5):
    if producao[i] > maior:
        maior = producao[i]
        indice_maior = i

    if producao[i] < menor:
        menor = producao[i]
        indice_menor = i

print("Maior valor:", maior)
print("Posição:", indice_maior)

print("Menor valor:", menor)
print("Posição:", indice_menor)
