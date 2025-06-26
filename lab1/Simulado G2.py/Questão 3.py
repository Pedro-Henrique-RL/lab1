def inserir_faturamento():
    faturamento = []
    for i in range(4):
        valor = float(input(f"Digite o faturamento da semana {i + 1}: R$ "))
        faturamento.append(valor)
    return faturamento

def exibir_faturamento(faturamento):
    for i in range(4):
        print(f"Semana {i + 1}: R$ {faturamento[i]:.2f}")

def calcular_dados(faturamento):
    media = sum(faturamento) / 4
    maior_valor = max(faturamento)
    semana_maior = faturamento.index(maior_valor) + 1

    print(f"\nMédia mensal de faturamento: R$ {media:.2f}")
    print(f"Semana com maior faturamento: Semana {semana_maior} (R$ {maior_valor:.2f})")

    print("\nCrescimento/queda semanal:")
    for i in range(3):
        anterior = faturamento[i]
        atual = faturamento[i + 1]
        variacao = ((atual - anterior) / anterior) * 100 if anterior != 0 else 0
        print(f"Semana {i + 1} → Semana {i + 2}: {variacao:.2f}%")

def alterar_semana(faturamento):
    semana = int(input("Digite o número da semana que deseja alterar (1 a 4): "))
    if 1 <= semana <= 4:
        novo_valor = float(input(f"Digite o novo faturamento da semana {semana}: R$ "))
        faturamento[semana - 1] = novo_valor
    else:
        print("Semana inválida.")

def main():
    faturamento = [0.0] * 4

    while True:
        print("\nMenu:")
        print("1 - Inserir faturamento semanal")
        print("2 - Exibir faturamento por semana")
        print("3 - Calcular e exibir dados")
        print("4 - Alterar faturamento de uma semana")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            faturamento = inserir_faturamento()
        elif opcao == "2":
            exibir_faturamento(faturamento)
        elif opcao == "3":
            calcular_dados(faturamento)
        elif opcao == "4":
            alterar_semana(faturamento)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

main()
