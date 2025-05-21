def ex14():
    guardioes = []
    invasores = []

    for i in range(5):
        guardioes.append(int(input(f"Força do guardião {i+1}: ")))

    while len(invasores) < 5:
        r = random.randint(1, 100)
        if r not in invasores:
            invasores.append(r)

    print("Guardioes:", guardioes)
    print("Invasores:", invasores)

    v_guardioes = 0
    v_invasores = 0

    for i in range(5):
        if guardioes[i] > invasores[i]:
            print(f"Batalha {i+1}: Guardião vence!")
            v_guardioes += 1
        else:
            print(f"Batalha {i+1}: Invasor resiste!")
            v_invasores += 1

    print(f"Placar final - Guardiões: {v_guardioes} | Invasores: {v_invasores}")
