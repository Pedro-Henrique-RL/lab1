valor_base = float(input("Digite o valor base do Ingresso:"))
print("1 - Ingresso normal (valor cheio)")
print("2 - Estudante (50 porcento de desconto)")
print("3 - Criança até 12 anos (paga 40 porcento do valor)")
print("4 - Idoso (paga 60 porcento do valor)")
opcao = input("Digite a opção desejada:")

if opcao == 1:
    print("O valor do Ingresso é:", valor_base)
elif opcao == 2:
    valor_base = valor_base / 2
    print("O valor do Ingresso é:", valor_base)
elif opcao == 3:
    valor = (valor_base * 40) / 100
    print("O valor do Ingresso é:", valor)
elif opcao == 4:
    valor = (valor_base * 60) / 100
    print("O valor do Ingresso é:", valor)
else:
    print("Essa opção não existe")
