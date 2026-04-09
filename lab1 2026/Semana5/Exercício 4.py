# EXERCÍCIO 4

respostas = 0

r1 = input("Treinou regularmente? (s/n): ")
if r1 == "s":
    respostas += 1

r2 = input("Treinos longos? (s/n): ")
if r2 == "s":
    respostas += 1

r3 = input("Seguiu dieta? (s/n): ")
if r3 == "s":
    respostas += 1

r4 = input("Competiu este ano? (s/n): ")
if r4 == "s":
    respostas += 1

r5 = input("Tem treinador? (s/n): ")
if r5 == "s":
    respostas += 1

if respostas == 5:
    print("Atleta de Elite")
elif respostas >= 3:
    print("Atleta Competitivo")
elif respostas == 2:
    print("Participante Casual")
else:
    print("Não Preparado")
