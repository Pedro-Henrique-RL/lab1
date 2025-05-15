vetor = []

for i in range(8):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

maiores_que_30 = []
soma_total = 0
soma_maiores = 0

for num in vetor:
    soma_total += num
    if num > 30:
        maiores_que_30.append(num)
        soma_maiores += num

print(f"Valores do vetor: {vetor}")
print(f"Quantidade de números maiores que 30: {len(maiores_que_30)}")
print(f"Soma dos números maiores que 30: {soma_maiores}")
print(f"Soma de todos os números: {soma_total}")
