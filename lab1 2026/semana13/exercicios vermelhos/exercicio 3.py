
def inserir_lote(lotes):
    codigo = int(input("Digite o código do lote (apenas pares): "))
    if codigo % 2 != 0:
        print("Erro! O código deve ser par.")
    else:
        lotes.append(codigo)
        print(f"Lote {codigo} inserido com sucesso!")

def listar_lotes(lotes):
    if len(lotes) == 0:
        print("Nenhum lote cadastrado.")
    else:
        print("Lotes cadastrados:")
        for lote in lotes:
            print(lote)

def retirar_lote(lotes):
    codigo = int(input("Digite o código do lote a retirar: "))
    if codigo in lotes:
        lotes.remove(codigo)
        print(f"Lote {codigo} retirado com sucesso!")
    else:
        print("Lote não encontrado.")

def limpar_lotes(lotes):
    lotes.clear()
    print("Todos os lotes foram removidos.")

def contar_maior_que_x(lotes):
    x = int(input("Digite o valor X para contar lotes com código maior que X: "))
    cont = 0
    for lote in lotes:
        if lote > x:
            cont += 1
    print(f"Existem {cont} lotes com código maior que {x}.")

def verificar_codigo(lotes):
    codigo = int(input("Digite o código a verificar: "))
    if codigo in lotes:
        print(f"O código {codigo} está presente.")
    else:
        print(f"O código {codigo} não está presente.")

def maior_menor(lotes):
    if len(lotes) == 0:
        print("Nenhum lote cadastrado.")
    else:
        print(f"Maior código: {max(lotes)}")
        print(f"Menor código: {min(lotes)}")

lotes = []
opcao = 0

while opcao != 8:
    print("\nMenu de gerenciamento de lotes (apenas pares):")
    print("1 - Inserir lote")
    print("2 - Listar lotes")
    print("3 - Retirar um lote")
    print("4 - Limpar todos os lotes")
    print("5 - Contar quantos lotes têm código maior que X")
    print("6 - Verificar se um código está presente")
    print("7 - Encontrar maior e menor código")
    print("8 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        inserir_lote(lotes)
    elif opcao == 2:
        listar_lotes(lotes)
    elif opcao == 3:
        retirar_lote(lotes)
    elif opcao == 4:
        limpar_lotes(lotes)
    elif opcao == 5:
        contar_maior_que_x(lotes)
    elif opcao == 6:
        verificar_codigo(lotes)
    elif opcao == 7:
        maior_menor(lotes)
    elif opcao == 8:
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")
