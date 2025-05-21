def ex13():
    vetor = []

    while True:
        print("\nMenu:")
        print("1 - Inserir item")
        print("2 - Listar itens")
        print("3 - Retirar item")
        print("4 - Retirar todos")
        print("5 - Contar itens > X")
        print("6 - Verificar número")
        print("7 - Maior e menor")
        print("8 - Sair")
        op = int(input("Escolha: "))

        if op == 1:
            num = int(input("Número par: "))
            if num % 2 != 0:
                print("Erro: apenas pares!")
            else:
                vetor.append(num)
        elif op == 2:
            print("Itens:", vetor)
        elif op == 3:
            num = int(input("Retirar qual número? "))
            if num in vetor:
                vetor.remove(num)
                print("Removido.")
            else:
                print("Não encontrado.")
        elif op == 4:
            vetor.clear()
            print("Todos removidos.")
        elif op == 5:
            x = int(input("Digite X: "))
            cont = sum(1 for i in vetor if i > x)
            print("Quantidade:", cont)
        elif op == 6:
            num = int(input("Número a verificar: "))
            print("Presente." if num in vetor else "Ausente.")
        elif op == 7:
            if not vetor:
                print("Vetor vazio.")
            else:
                maior = menor = vetor[0]
                for i in vetor[1:]:
                    if i > maior:
                        maior = i
                    if i < menor:
                        menor = i
                print("Maior:", maior, "Menor:", menor)
        elif op == 8:
            break
        else:
            print("Opção inválida.")
