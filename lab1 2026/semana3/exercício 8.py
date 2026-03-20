valor = int(input("Digite o valor da compra: "))

if valor > 100:
    desconto = valor * 0.10
    valorF = valor - desconto
    print("O valor com desconto é: ",valorF)
else:
    print("Não houve desconto, entao o valor é: ",valor)
