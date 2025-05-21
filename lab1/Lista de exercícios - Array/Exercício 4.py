def ex4():
    vetor = []
    for _ in range(5):
        vetor.append(int(input("Digite um número: ")))
    maior = vetor[0]
    menor = vetor[0]
    pos_maior = 0
    pos_menor = 0
    for i in range(1, 5):
        if vetor[i] > maior:
            maior = vetor[i]
            pos_maior = i
        if vetor[i] < menor:
            menor = vetor[i]
            pos_menor = i
    print("Maior:", maior, "na posição", pos_maior)
    print("Menor:", menor, "na posição", pos_menor)
