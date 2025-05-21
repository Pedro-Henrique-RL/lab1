def ex6():
    vetor = []
    for _ in range(6):
        vetor.append(int(input("Digite um número: ")))
    constante = int(input("Digite a constante: "))
    resultado = []
    for i in range(6):
        resultado.append(vetor[i] * constante)
    print("Resultado:", resultado)
