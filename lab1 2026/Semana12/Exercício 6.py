
saldo = 0

def mostrar_menu():
    print("\n1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")

def sacar():
    global saldo

    valor = float(input("Digite o valor para sacar: "))

    if valor <= saldo:
        saldo = saldo - valor
        print("Saque realizado")
    else:
        print("Saldo insuficiente")

def depositar():
    global saldo

    valor = float(input("Digite o valor para depositar: "))

    saldo = saldo + valor

    print("Depósito realizado")

def mostrar_saldo():
    print("Saldo atual:", saldo)

opcao = 0

while opcao != 4:

    mostrar_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        sacar()

    elif opcao == 2:
        depositar()

    elif opcao == 3:
        mostrar_saldo()

    elif opcao == 4:
        print("Sistema encerrado")

    else:
        print("Opção inválida")
