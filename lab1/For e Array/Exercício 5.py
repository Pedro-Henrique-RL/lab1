vetor_a = []

while len(vetor_a) < 10:
    valor = int(input(f"Digite o {len(vetor_a)+1}º valor (distinto): "))
    if valor not in vetor_a:
        vetor_a.append(valor)
    else:
        print("Valor já digitado. Digite outro.")

vetor_b = []

for i in range(9, -1, -1):
    vetor_b.append(vetor_a[i])

print(f"Vetor A: {vetor_a}")
print(f"Vetor B (inverso): {vetor_b}")
