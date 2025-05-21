def ex12():
    vetor = []
    while len(vetor) < 15:
        num = int(input("Digite um número: "))
        if num in vetor:
            print("Valor repetido! Digite outro.")
        else:
            vetor.append(num)
    print("Vetor completo:", vetor)
