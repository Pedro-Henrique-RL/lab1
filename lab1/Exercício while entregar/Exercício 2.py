saldo = float(input("Digite o saldo inicial: "))
opcao = 0

while opcao != 4:
    print("\n1 - Sacar")
    print("2 - Depositar")
    print("3 - Ver saldo")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Valor para sacar: "))
        if valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente.")
    elif opcao == 2:
        valor = float(input("Valor para depositar: "))
        saldo += valor
    elif opcao == 3:
        print("Saldo atual: R$", saldo)
