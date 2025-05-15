masculino = 0
feminino = 0
idade_maior = 0
feminino_18_35_verde_loiro = 0
olhos_azuis = olhos_verdes = olhos_castanhos = 0
cabelos_loiros = cabelos_castanhos = cabelos_pretos = 0

for i in range(15):
    print(f"\nPessoa {i+1}:")
    sexo = input("Sexo (M/F): ").upper()
    olhos = input("Cor dos olhos (A/V/C): ").upper()
    cabelos = input("Cor dos cabelos (L/C/P): ").upper()
    idade = int(input("Idade: "))

    if idade > idade_maior:
        idade_maior = idade

    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1
        if 18 <= idade <= 35 and olhos == 'V' and cabelos == 'L':
            feminino_18_35_verde_loiro += 1

    if olhos == 'A':
        olhos_azuis += 1
    elif olhos == 'V':
        olhos_verdes += 1
    elif olhos == 'C':
        olhos_castanhos += 1

    if cabelos == 'L':
        cabelos_loiros += 1
    elif cabelos == 'C':
        cabelos_castanhos += 1
    elif cabelos == 'P':
        cabelos_pretos += 1

print(f"\nMaior idade do grupo: {idade_maior}")
print(f"Quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros: {feminino_18_35_verde_loiro}")
print(f"Porcentagem com olhos azuis: {olhos_azuis / 15 * 100:.1f}%")
print(f"Porcentagem com olhos verdes: {olhos_verdes / 15 * 100:.1f}%")
print(f"Porcentagem com olhos castanhos: {olhos_castanhos / 15 * 100:.1f}%")
print(f"Porcentagem de loiros: {cabelos_loiros / 15 * 100:.1f}%")
print(f"Porcentagem de castanhos: {cabelos_castanhos / 15 * 100:.1f}%")
print(f"Porcentagem de pretos: {cabelos_pretos / 15 * 100:.1f}%")
print(f"Porcentagem de masculinos: {masculino / 15 * 100:.1f}%")
print(f"Porcentagem de femininos: {feminino / 15 * 100:.1f}%")
