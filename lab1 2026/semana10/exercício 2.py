pares = 0
impares = 0
zeros = 0


for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    
    if numero == 0:
        zeros = zeros + 1
    elif numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
print("Quantidade de zeros:", zeros)
