total_gasolina = 0
total_diesel = 0

opcao = 0

while opcao != 2:
    print("1. Vender combustível")
    print("2. Sair")
    
    opcao = int(input("Escolha: "))
    
    if opcao == 1:
        print("1. Gasolina (R$ 6.89)")
        print("2. Diesel (R$ 4.80)")
        
        tipo = int(input("Escolha o combustível: "))
        
        if tipo == 1 or tipo == 2:
            litros = float(input("Litros abastecidos: "))
            valor_pago = float(input("Valor pago: "))
            
            if tipo == 1:
                total = litros * 6.89
                total_gasolina += litros
            else:
                total = litros * 4.80
                total_diesel += litros
            
            print("Total a pagar: R$", round(total, 2))
            
            if valor_pago > total:
                print("Troco: R$", round(valor_pago - total, 2))
            elif valor_pago < total:
                print("Faltou: R$", round(total - valor_pago, 2))
            else:
                print("Pagamento exato")
        
        else:
            print("Opção inválida")
    
    elif opcao == 2:
        print("Encerrando...")
    
    else:
        print("Opção inválida")
