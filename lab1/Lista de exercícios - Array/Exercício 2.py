def ex2():
    vetor = []
    for _ in range(5):
        vetor.append(int(input("Digite um número: ")))
    for i in range(4, -1, -1):
        print(vetor[i], end=" ")
    print()
