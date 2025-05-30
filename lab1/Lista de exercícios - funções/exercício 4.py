def soma_naturais(n):
    if n < 0:
        return 0
    return sum(range(n + 1))

numero = int(input("Digite um número natural: "))
resultado = soma_naturais(numero)
print(f"A soma de todos os números naturais menores ou iguais a {numero} é {resultado}.")
