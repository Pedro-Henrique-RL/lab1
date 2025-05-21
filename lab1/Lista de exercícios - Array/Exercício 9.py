def ex9():
    vetor = []
    for _ in range(10):
        vetor.append(random.randint(1, 50))
    pares = 0
    impares = 0
    for num in vetor:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Pares:", pares)
    print("Ímpares:", impares)
