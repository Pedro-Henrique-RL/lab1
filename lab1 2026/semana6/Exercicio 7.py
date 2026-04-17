contador = 0
soma_idades = 0

while contador < 15:
    idade = int(input("Digite a idade do estudante: "))

    if idade < 0:
        print("Idade inválida! Digite novamente.")
    else:
        soma_idades = soma_idades + idade
        contador = contador + 1

media = soma_idades / 15

if media >= 0 and media <= 25:
    print("Média da turma:", media)
    print("Classificação: turma jovem")
elif media >= 26 and media <= 60:
    print("Média da turma:", media)
    print("Classificação: turma adulta")
elif media > 60:
    print("Média da turma:", media)
    print("Classificação: turma idosa")
else:
    print("Erro no cálculo.")
