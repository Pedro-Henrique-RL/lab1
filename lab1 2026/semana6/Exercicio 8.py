plantacao_A = 80000
plantacao_B = 200000

taxa_A = 0.03
taxa_B = 0.015

anos = 0

while plantacao_A < plantacao_B:
    plantacao_A = plantacao_A + (plantacao_A * taxa_A)
    plantacao_B = plantacao_B + (plantacao_B * taxa_B)
    anos = anos + 1

if plantacao_A >= plantacao_B:
    print("A plantação A alcançou ou ultrapassou a B.")
    print("Isso ocorreu em", anos, "anos.")
elif plantacao_A < plantacao_B:
    print("A plantação A ainda não alcançou a B.")
else:
    print("Erro no cálculo.")
