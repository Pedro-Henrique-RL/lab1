print("Números de 1 a 10:")

for numero in range(1, 11):
    print(numero)

soma = 0  

for i in range(10):  
    numero = float(input(f"Digite o {i+1}º número: ")) 
    soma = soma + numero  

media = soma / 10 
print("A média dos números é:", media)

termo1 = 0
termo2 = 1

print("Sequência de Fibonacci até o 10º termo:")

for i in range(10):
    print(termo1)
    proximo_termo = termo1 + termo2
    termo1 = termo2  
    termo2 = proximo_termo
