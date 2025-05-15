vetor = []

while True:
    print("\nMenu:")
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para inserir: ")
        vetor.append(item)
    elif opcao == "2":
        if len(vetor) > 0:
            item = input("Digite o item para retirar: ")
            if item in vetor:
                vetor.remove(item)
            else:
                print("Item não encontrado.")
        else:
            print("Vetor vazio.")
    elif opcao == "3":
        if len(vetor) > 0:
            print("Itens no vetor:")
            for item in vetor:
                print(item)
        else:
            print("Vetor vazio.")
    elif opcao == "4":
        vetor.clear()
        print("Todos os itens foram retirados.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
