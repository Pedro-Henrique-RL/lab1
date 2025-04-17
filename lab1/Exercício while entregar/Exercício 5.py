i = 0
soma_salario = 0
maior_idade = 0
menor_idade = 200
mulheres_pobres = 0

while i < 10:
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    salario = float(input("Salário: "))
    
    soma_salario += salario

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    if sexo == "F" and salario <= 10000:
        mulheres_pobres += 1

    i += 1

print("Média salarial:", soma_salario / 10)
print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)
print("Mulheres com salário até R$10000:", mulheres_pobres)
