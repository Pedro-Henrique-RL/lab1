saldo = 0
opcao = 0

while saldo <= 0:
    saldo = int(input("Digite o saldo inicial: "))

# 1 - sacar
# 2 - depositar
# 3 - saldo 
# 4 - sair

while opcao != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = float(input("Digite uma opção: "))

if opcao == 1:
    valor = float(input("Valor para sacar: "))
    if valor <= saldo:
        saldo = saldo - valor
        print("Saldo atual", saldo)
    else:
        print("Saldo insuficiente!")
elif opcao == 2:
    valor = float(input("Digite o valor a ser depositado: "))
    if saldo >= 0:
        saldo = saldo + valor
elif opcao == 3:
    print("Saldo:", saldo)
elif opcao == 4:
    print("Até mais!")
else:
    print("Opção invalida!")
