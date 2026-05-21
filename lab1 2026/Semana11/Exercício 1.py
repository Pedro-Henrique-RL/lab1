vetor = []

for i in range(8):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)

print("\nValores no vetor:", vetor)

maior_30 = 0
soma_maior_30 = 0
soma_total = 0

for num in vetor:
    soma_total += num
    if num > 30:
        maior_30 += 1
        soma_maior_30 += num

print(f"\nQuantidade de números maiores que 30: {maior_30}")
print(f"Soma dos números maiores que 30: {soma_maior_30}")
print(f"Soma de todos os números: {soma_total}")
