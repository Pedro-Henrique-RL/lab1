i = 0
elevador_a = 0
elevador_b = 0
elevador_c = 0

while i < 10:
    elevador = input(f"Morador {i+1} - Elevador (A, B ou C): ").upper()
    if elevador == 'A':
        elevador_a += 1
    elif elevador == 'B':
        elevador_b += 1
    elif elevador == 'C':
        elevador_c += 1
    else:
        print("Elevador inválido.")
        continue
    i += 1

print("Elevador A:", elevador_a, "-", (elevador_a / 10) * 100, "%")
print("Elevador B:", elevador_b, "-", (elevador_b / 10) * 100, "%")
print("Elevador C:", elevador_c, "-", (elevador_c / 10) * 100, "%")
