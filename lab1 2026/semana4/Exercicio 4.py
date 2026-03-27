inscricao = float(input("Digite o valor da inscrição: "))

print("1 - À vista.")
print("2 - Em 2 vezes.")
print("3 - Em 3 vezes.")

opcao = int(input("Digite qual opção deseja: "))

if opcao == 1:
    print("O valor da inscrição é:", inscricao)
elif opcao == 2:
    print("O valor da inscrição é:", inscricao)
    parcelas = inscricao / 2
    print("Cada parcela é:", parcelas)
elif opcao == 3:
    print("O valor da inscrição é:", inscricao)
    parcelas = inscricao / 3
    print("Cada parcela é:", parcelas)
else:
    print("Essa opção não existe")
