nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço (anos): "))

if tempo_servico >= 5 and salario <= 2000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print(f"{nome} terá um aumento de R$ {aumento:.2f}. Novo salário: R$ {novo_salario:.2f}")
