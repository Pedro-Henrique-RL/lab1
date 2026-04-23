i = 0
contador = 0

while i < 10:
    temp = float(input("Temperatura: "))
    if 15 <= temp <= 25:
        contador += 1
    i += 1

print("Temperaturas entre 15 e 25:", contador)
