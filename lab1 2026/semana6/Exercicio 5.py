oliveiras = int(input("Digite o número total de oliveiras plantadas: "))

while oliveiras < 0:
    print("Número inválido! Digite um valor maior ou igual a zero.")
    oliveiras = int(input("Digite o número total de oliveiras plantadas: "))

litros = (oliveiras * 5) / 100

if oliveiras == 0:
    print("Nenhuma produção de azeite.")
elif oliveiras > 0:
    print("Produção anual estimada de azeite:", litros, "litros.")
else:
    print("Erro no cálculo.")
