def ex1():
    vetor = [i for i in range(1, 11)]
    for i in range(len(vetor)-1, -1, -1):
        print(vetor[i], end=" ")
    print()
