
total_oliveiras = int(input("Digite o número total de oliveiras: "))
fileiras = int(input("Digite o número de fileiras disponíveis: "))

while fileiras <= 0:
    print("Número de fileiras inválido! Digite um valor maior que zero.")
    fileiras = int(input("Digite o número de fileiras disponíveis: "))

oliveiras_por_fileira = total_oliveiras // fileiras
sobra = total_oliveiras % fileiras

if sobra == 0:
    print("Não haverá sobra de mudas.")
    print("Cada fileira terá", oliveiras_por_fileira, "oliveiras.")
elif sobra > 0:
    print("Cada fileira terá", oliveiras_por_fileira, "oliveiras.")
    print("Haverá sobra de", sobra, "mudas.")
else:
    print("Erro no cálculo.")
