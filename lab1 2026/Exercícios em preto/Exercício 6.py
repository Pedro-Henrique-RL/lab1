quantidade = 1

print("Loja das Oliveiras – Tabela de preços")

while quantidade <= 50:
    preco = quantidade * 1.99
    print(quantidade, "muda(s) – R$", round(preco, 2))
    
    quantidade = quantidade + 1
