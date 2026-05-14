
maior_idade = 0

cont_verde_preto = 0

olhos_azuis = 0
olhos_verdes = 0
olhos_castanhos = 0

cabelo_loiro = 0
cabelo_castanho = 0
cabelo_preto = 0

sexo_m = 0
sexo_f = 0

total = 15
contador = 1

while contador <= total:

    sexo = input("Sexo (M/F): ")
    olhos = input("Cor dos olhos (A/V/C): ")
    cabelo = input("Cor do cabelo (L/C/P): ")
    idade = int(input("Idade: "))

    if idade > maior_idade:
        maior_idade = idade

    if idade >= 18 and idade <= 35 and olhos == "V" and cabelo == "P":
        cont_verde_preto = cont_verde_preto + 1

    if olhos == "A":
        olhos_azuis = olhos_azuis + 1
    elif olhos == "V":
        olhos_verdes = olhos_verdes + 1
    elif olhos == "C":
        olhos_castanhos = olhos_castanhos + 1

    if cabelo == "L":
        cabelo_loiro = cabelo_loiro + 1
    elif cabelo == "C":
        cabelo_castanho = cabelo_castanho + 1
    elif cabelo == "P":
        cabelo_preto = cabelo_preto + 1

    if sexo == "M":
        sexo_m = sexo_m + 1
    elif sexo == "F":
        sexo_f = sexo_f + 1

    contador = contador + 1

print("Maior idade:", maior_idade)

print("Quantidade entre 18 e 35 anos com olhos verdes e cabelos pretos:", cont_verde_preto)

print("Porcentagem olhos azuis:", (olhos_azuis / total) * 100, "%")
print("Porcentagem olhos verdes:", (olhos_verdes / total) * 100, "%")
print("Porcentagem olhos castanhos:", (olhos_castanhos / total) * 100, "%")

print("Porcentagem cabelos loiros:", (cabelo_loiro / total) * 100, "%")
print("Porcentagem cabelos castanhos:", (cabelo_castanho / total) * 100, "%")
print("Porcentagem cabelos pretos:", (cabelo_preto / total) * 100, "%")

print("Porcentagem masculino:", (sexo_m / total) * 100, "%")
print("Porcentagem feminino:", (sexo_f / total) * 100, "%")
