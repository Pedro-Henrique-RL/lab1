valor = float(input("Digite o valor do carro:"))

print("1 - Pagamento à vista (4 porcento de desconto)")
print("2 - Pagamento em 12x (2 porcento de juros)")
print("3 - Pagamento em 24x (7 porcento de juros)")
print("4 - Pagamento em 36x (15 porcento de juros)")
opcao = int(input("Digite a opção escolhida:"))

if opcao == 1:
    valor_final = valor * 0.96 
    print("Valor final é:", valor_final)
elif opcao == 2:
    valor_final = valor * 1.02
    parcelas = valor_final / 12
    print("O valor final é:", valor_final, "E cada parcela ficou:", parcelas)
elif opcao == 3:
    valor_final = valor * 1.07
    parcelas = valor_final / 24
    print("O valor final é:", valor_final, "E cada parcela ficou:", parcelas)    
elif opcao == 4:
    valor_final = valor * 1.15
    parcelas = valor_final / 36
    print("O valor final é:", valor_final, "E cada parcela ficou:", parcelas)    
else:
    print("Essa opção não existe")
