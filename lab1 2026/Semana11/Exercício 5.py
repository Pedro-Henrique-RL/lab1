itens = []

while True:
    print("\n----- MENU -----")
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o item a inserir: ")
        itens.append(item)
        print(f"Item '{item}' inserido.")
    
    elif opcao == "2":
        if len(itens) == 0:
            print("A lista está vazia. Nada para retirar.")
        else:
            item = input("Digite o item a retirar: ")
            if item in itens:
                itens.remove(item)
                print(f"Item '{item}' removido.")
            else:
                print("Item não encontrado.")
    
    elif opcao == "3":
        if len(itens) == 0:
            print("A lista está vazia.")
        else:
            print("\nItens na lista:")
            for item in itens:
                print(item)
    
    elif opcao == "4":
        itens.clear()
        print("Todos os itens foram removidos.")
    
    elif opcao == "5":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida! Digite um número de 1 a 5.")
