caixa = float(input("Dinheiro em caixa: "))
opcao = 0

while opcao != 4:
    print("\n1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Ver caixa")
    print("4 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        valor = float(input("Valor da venda: "))
        caixa += valor
    elif opcao == 2:
        valor = float(input("Valor para retirar: "))
        if valor <= caixa:
            caixa -= valor
        else:
            print("Valor indisponível.")
    elif opcao == 3:
        print("Dinheiro em caixa:", caixa)
