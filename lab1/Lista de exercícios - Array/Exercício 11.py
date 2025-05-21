def ex11():
    vetor = []
    for _ in range(5):
        vetor.append(int(input("Digite um número: ")))
    distinto = True
    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            if vetor[i] == vetor[j]:
                distinto = False
    print("Todos distintos?" , "Sim" if distinto else "Não")
