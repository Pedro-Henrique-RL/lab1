def ler_tamanho_array():
    tamanho = int(input("Digite o tamanho do array: "))
    return tamanho

def preencher_array(tamanho):
    array = []
    for i in range(tamanho):
        valor = int(input(f"Digite o {i + 1}º número: "))
        array.append(valor)
    return array

def mostrar_array(array):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Mostrar todos os valores")
        print("2 - Mostrar valores ímpares e múltiplos de 3")
        print("3 - Mostrar valores nas posições ímpares e múltiplos de 5")
        print("4 - Mostrar os valores invertidos")
        print("5 - Voltar ao menu principal")
        opcao = input("Opção: ")

        if opcao == "1":
            for valor in array:
                print(valor)
        elif opcao == "2":
            for valor in array:
                if valor % 2 == 1 and valor % 3 == 0:
                    print(valor)
        elif opcao == "3":
            for i in range(1, len(array), 2):
                if array[i] % 5 == 0:
                    print(array[i])
        elif opcao == "4":
            for valor in reversed(array):
                print(valor)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def main():
    while True:
        print("\nMenu:")
        print("1 - Criar array")
        print("2 - Mostrar array")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tamanho = ler_tamanho_array()
            array = preencher_array(tamanho)
        elif escolha == "2":
            try:
                mostrar_array(array)
            except NameError:
                print("Você precisa criar o array primeiro.")
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")

main()
