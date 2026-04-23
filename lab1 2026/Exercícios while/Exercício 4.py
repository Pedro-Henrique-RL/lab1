i = 0
soma_salario = 0
mais_novo = 999
mais_velho = 0
atacantes_ate_10k = 0
cont_atacante = 0
cont_defensor = 0

while i < 10:
    idade = int(input("Idade: "))
    posicao = input("Posição (A/D): ").upper()
    salario = float(input("Salário: "))

    soma_salario += salario

    if idade < mais_novo:
        mais_novo = idade
    if idade > mais_velho:
        mais_velho = idade

    if posicao == "A":
        cont_atacante += 1
        if salario <= 10000:
            atacantes_ate_10k += 1
    elif posicao == "D":
        cont_defensor += 1

    i += 1

print("Média salários:", soma_salario / 10)
print("Mais novo:", mais_novo)
print("Mais velho:", mais_velho)
print("Atacantes até 10k:", atacantes_ate_10k)
print("Atacantes:", cont_atacante)
print("Defensores:", cont_defensor)
