# EXERCÍCIO 1

nome = input("Nome do treinador: ")
salario = float(input("Salário atual: "))
anos = int(input("Anos de serviço: "))

if anos >= 5 and salario <= 2000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print("Nome:", nome)
print("Aumento:", aumento)
print("Novo salário:", novo_salario)
