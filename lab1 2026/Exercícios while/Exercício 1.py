ingressos = 100
opcao = 0

while opcao != 4:
    print("\n1 - Diminuir ingressos")
    print("2 - Adicionar ingressos")
    print("3 - Mostrar disponíveis")
    print("4 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        qtd = int(input("Quantidade para diminuir: "))
        if qtd <= ingressos:
            ingressos -= qtd
        else:
            print("Não há ingressos suficientes.")
    elif opcao == 2:
        qtd = int(input("Quantidade para adicionar: "))
        ingressos += qtd
    elif opcao == 3:
        print("Ingressos disponíveis:", ingressos)
