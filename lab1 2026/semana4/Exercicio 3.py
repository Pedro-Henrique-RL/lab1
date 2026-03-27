time1 = int(input("Digite a pontuação do time 1:"))
time2 = int(input("Digite a pontuação do time 2:"))

if time1 > time2:
    print("O time 1 venceu")
elif time1 == time2:
    print("Empate")
else:
    print("Time 2 venceu")
