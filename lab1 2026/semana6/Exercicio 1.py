dia = 1
total = 0

maior = -1
menor = 99999
dia_maior = 0
dia_menor = 0

while dia <= 7:
    quantidade = int(input("Informe a quantidade de oliveiras do dia:"))
    
    total += quantidade

    if quantidade > maior:
        maior = quantidade
        dia_maior = dia
    if quantidade < menor:
        menor = quantidade
        dia_menor = dia
    dia += 1

print("Resultado da semana:")
print("Total de oliveiras:", total)
print("Maior colheita: Dia", dia_maior, "com", maior)
print("Menor colheita: Dia", dia_menor, "com", menor)
