opcao = 0
soma_idade = 0
soma_altura = 0
contador = 0

while opcao != 3:
    print("\n1 - Cadastrar pessoa")
    print("2 - Mostrar média parcial")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        soma_idade += idade
        soma_altura += altura
        contador += 1
    elif opcao == 2:
        if contador > 0:
            print("Média idade:", soma_idade / contador)
            print("Média altura:", soma_altura / contador)
        else:
            print("Nenhum dado cadastrado.")

if contador > 0:
    print("\nMédia final idade:", soma_idade / contador)
    print("Média final altura:", soma_altura / contador)
