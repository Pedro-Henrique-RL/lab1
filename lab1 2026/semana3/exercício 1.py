horas = float(input("Digite as horas trabalhadas do mês:"))
salario = horas * 35

if salario < 1000:
    aumento = salario + 300
    print("Seu salario esse mes é R$",(aumento))
else:
    print("Seu salario esse mes é R$",salario)
