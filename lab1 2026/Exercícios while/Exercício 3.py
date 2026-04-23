i = 0
soma = 0
menos_30 = 0
entre_30_60 = 0

while i < 7:
    tempo = float(input(f"Tempo do corredor {i+1}: "))
    soma += tempo

    if tempo < 30:
        menos_30 += 1
    if 30 <= tempo <= 60:
        entre_30_60 += 1

    i += 1

print("Tempo médio:", soma / 7)
print("Menos de 30 min:", menos_30)
print("Porcentagem entre 30 e 60:", (entre_30_60 / 7) * 100, "%")
