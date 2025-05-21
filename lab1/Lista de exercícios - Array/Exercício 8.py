def ex8():
    vetor = []
    for _ in range(5):
        vetor.append(int(input("Digite um número: ")))
    num = int(input("Digite o número para verificar: "))
    if num in vetor:
        print("Está presente.")
    else:
        print("Não está presente.")
