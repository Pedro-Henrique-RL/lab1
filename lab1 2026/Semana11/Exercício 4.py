A = []
B = [0] * 10

print("Digite 10 valores inteiros distintos:\n")

while len(A) < 10:
    num = int(input(f"Digite o {len(A)+1}º valor: "))
    if num in A:
        print("Valor repetido! Digite um valor diferente.")
    else:
        A.append(num)

for i in range(10):
    B[i] = A[9 - i]

print("\nVetor A:", A)
print("Vetor B (ordem inversa):", B)
