# Idade
idade = -1
while idade < 0 or idade > 150:
    idade = int(input("Digite a idade (0 a 150): "))
    
    if idade < 0 or idade > 150:
        print("Idade inválida")

# Salário
salario = 0
while salario <= 0:
    salario = float(input("Digite o salário (maior que 0): "))
    
    if salario <= 0:
        print("Salário inválido")

# Sexo
sexo = ""
while sexo != "f" and sexo != "m":
    sexo = input("Digite o sexo (f/m): ")
    
    if sexo != "f" and sexo != "m":
        print("Sexo inválido")

# Estado civil
estado = ""
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    estado = input("Digite o estado civil (s/c/v/d): ")
    
    if estado != "s" and estado != "c" and estado != "v" and estado != "d":
        print("Estado civil inválido")

print("Dados cadastrados com sucesso!")
