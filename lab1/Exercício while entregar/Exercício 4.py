i = 0
soma = 0
maiores = 0
entre_10_30 = 0

while i < 7:
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    soma += idade
    if idade >= 18:
        maiores += 1
    if 10 <= idade <= 30:
        entre_10_30 += 1
    i += 1

print("Média das idades:", soma / 7)
print("Maiores de idade:", maiores)
print("Porcentagem entre 10 e 30 anos:", (entre_10_30 / 7) * 100, "%")
