
def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)

    valor_final = custo + imposto

    return valor_final

custo = float(input("Digite o custo do produto: "))
taxa = float(input("Digite a taxa de imposto (%): "))

resultado = somaImposto(taxa, custo)

print("Valor com imposto:", resultado)
