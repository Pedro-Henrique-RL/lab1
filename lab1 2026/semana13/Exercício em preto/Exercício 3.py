producao = []

for i in range(5):
    valor = float(input("Digite a produção: "))
    producao.append(valor)

print("Ordem inversa:")

for i in range(len(producao) - 1, -1, -1):
    print(producao[i])
