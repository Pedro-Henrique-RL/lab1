print("--- Escolha seu Kit ---")
print("1 - Kit Básico (R$100.00)")
print("2 - Kit Plus (R$120.00)")
print("3 - Kit Premium (R$150.00)")

opcao = int(input("Digite o número do kit desejado: "))
valor_pago = float(input("Digite o valor em R$ que você está entregando: "))

if opcao == 1:
    nome_kit = "Kit Básico (Número de peito + medalha)"
    valor_kit = 100.00
elif opcao == 2:
    nome_kit = "Kit Plus (Número de peito + medalha + camiseta)"
    valor_kit = 120.00
elif opcao == 3:
    nome_kit = "Kit Premium (Número de peito + medalha + camiseta + squeeze + boné)"
    valor_kit = 150.00
else:
    nome_kit = "Opção Inválida"
    valor_kit = 0.0

if valor_kit == 0.0:
    print("Erro: Opção de kit inválida.")
elif valor_pago >= valor_kit:
    troco = valor_pago - valor_kit
    print("-" * 30)
    print("Kit selecionado:", nome_kit)
    print("Pagamento confirmado!")
    print("Troco: R$", troco)
    print("-" * 30)
else:
    falta = valor_kit - valor_pago
    print("-" * 30)
    print("Valor insuficiente!")
    print("Faltam R$", falta, "para o", nome_kit)
    print("-" * 30)
