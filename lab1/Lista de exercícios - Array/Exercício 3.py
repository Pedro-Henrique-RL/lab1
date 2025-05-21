def ex3():
    vetor = []
    for _ in range(5):
        vetor.append(int(input("Digite um número: ")))
    soma = 0
    for num in vetor:
        soma += num
    media = soma / 5
    print("Soma:", soma)
    print("Média:", media)
