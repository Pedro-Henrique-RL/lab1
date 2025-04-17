i = 0
maiores = 0

while i < 10:
    idade = int(input(f"Idade da pessoa {i+1}: "))
    if idade >= 18:
        maiores += 1
    i += 1

print("Quantidade com 18 anos ou mais:", maiores)
